from django.http import JsonResponse, HttpResponse
from django.utils.html import escape, linebreaks
from django.db import transaction
from .models import Question, Review, PopularModel, ReviewPhoto
from .serializers import (
    QuestionSerializer,
    ReviewSerializer,
    PopularModelSerializer,
    OrderSerializer,
)
from .review_photos import MAX_PHOTOS, PhotoError, process_photo
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

import hmac
import hashlib
import json
import logging
import requests
from django.conf import settings

logger = logging.getLogger(__name__)

# (подключение, чтение) в секундах для внешних API: зависший Bitrix/Telepush не должен держать воркер gunicorn.
EXTERNAL_TIMEOUT = (5, 15)

SERVER_ERROR = {"error": "Внутренняя ошибка сервера, попробуйте позже"}


def aggregate_data(request):
    try:
        questions = Question.objects.all()
        reviews = Review.objects.select_related("sofa").filter(published=True)
        popular_models = PopularModel.objects.select_related("sofa").all()

        questions_data = QuestionSerializer(questions, many=True).data
        reviews_data = ReviewSerializer(reviews, many=True).data
        popular_models_data = PopularModelSerializer(popular_models, many=True).data

        aggregated_data = {
            "questions": questions_data,
            "reviews": reviews_data,
            "popular_models": popular_models_data,
        }

        return JsonResponse(aggregated_data, safe=False)

    except Exception:
        logger.exception("service aggregate_data failed")
        return JsonResponse(SERVER_ERROR, status=500)


def get_reviews(request):
    try:
        reviews = Review.objects.select_related("sofa").filter(published=True)

        reviews_data = ReviewSerializer(reviews, many=True).data

        aggregated_data = {
            "reviews": reviews_data,
        }

        return JsonResponse(aggregated_data, safe=False)

    except Exception:
        logger.exception("get_reviews failed")
        return JsonResponse(SERVER_ERROR, status=500)


def _bad_request(message):
    return JsonResponse({"error": message}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes((AllowAny,))
def create_review(request):
    author = (request.POST.get("author") or "").strip()
    text = (request.POST.get("review") or "").strip()
    photo_files = request.FILES.getlist("photos")

    if not 2 <= len(author) <= 100:
        return _bad_request("Имя должно быть от 2 до 100 символов")
    if not 3 <= len(text) <= 5000:
        return _bad_request("Отзыв должен быть от 3 до 5000 символов")
    if len(photo_files) > MAX_PHOTOS:
        return _bad_request(f"Можно приложить не больше {MAX_PHOTOS} фото")

    try:
        # Сначала проверяем все фото, и только потом что-то пишем: битый файл не оставит полуотзыв.
        photos = [process_photo(f) for f in photo_files]
    except PhotoError as e:
        return _bad_request(str(e))

    try:
        with transaction.atomic():
            # Поле review выводится на сайте через v-html и открывается в CKEditor в админке,
            # поэтому текст от анонима храним только как экранированный: <p>, <br> и ничего больше.
            new_review = Review.objects.create(
                author=author,
                review=linebreaks(escape(text)),
                published=False,
            )
            for i, photo in enumerate(photos):
                review_photo = ReviewPhoto(field=new_review, order=i + 1)
                review_photo.photo.save(photo.name, photo, save=False)
                review_photo.save()
    except Exception:
        logger.exception("create_review failed")
        return JsonResponse(SERVER_ERROR, status=500)

    return JsonResponse(ReviewSerializer(new_review).data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes((AllowAny,))
def create_order(request):
    hmac_key = settings.HMAC_KEY
    received_signature = request.META.get("HTTP_X_SIGNATURE")

    if received_signature:
        payload = json.dumps(request.data, separators=(",", ":"), ensure_ascii=False)
        expected_signature = hmac.new(bytes(hmac_key, 'utf-8'), msg=payload.encode("utf-8"), digestmod=hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected_signature, received_signature):
            return HttpResponse(status=403)
    else:
        return HttpResponse(status=403)

    order_payload = request.data.get("request") if isinstance(request.data, dict) else None
    if not isinstance(order_payload, dict):
        return _bad_request("Некорректный запрос")

    serializer = OrderSerializer(data=order_payload)
    if not serializer.is_valid():
        # Ошибки валидации полей (имя, телефон) — пользовательские, их отдаём как есть.
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    order_data = serializer.data

    # Заявка уже в БД: сбой уведомления в Telegram не должен мешать отправке в Bitrix.
    try:
        telepush_send(order_data)
    except Exception:
        logger.exception("telepush failed for order id=%s", order_data.get("id"))

    bitrix_data = {
        "fields[TITLE]": f"{order_data.get('name')} - kamamebel.com",
        "fields[NAME]": order_data.get("name"),
        "fields[PHONE][0][VALUE]": order_data.get("number"),
        "fields[SOURCE_ID]": "WEB",
        "fields[COMMENTS]": f'Клиент оставил сообщение "{order_data.get("message")}"' if order_data.get("message") else 'Клиент не оставил сообщения',
        "fields[ASSIGNED_BY_ID]": "1",
        "fields[OPENED]": "Y",
    }
    bitrix_webhook_url = f"{settings.BITRIX_WEBHOOK_URL}/crm.lead.add.json"

    try:
        # params= кодирует значения: «&» или «=» в имени/сообщении не сломают и не подменят поля лида.
        response = requests.post(bitrix_webhook_url, params=bitrix_data, timeout=EXTERNAL_TIMEOUT)
    except requests.RequestException as e:
        # Только тип ошибки: в тексте исключения есть URL вебхука с секретом.
        logger.error("bitrix request failed for order id=%s: %s", order_data.get("id"), type(e).__name__)
        return JsonResponse(SERVER_ERROR, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if response.status_code != 200:
        logger.error("bitrix returned %s for order id=%s: %.500s",
                     response.status_code, order_data.get("id"), response.text)
        return JsonResponse(SERVER_ERROR, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


def telepush_send(order_data):
    recipient_token = settings.RECIPIENT_TOKEN

    message = "Клиент не оставил сообщения"
    if order_data.get("message"):
        message = f"Клиент оставил сообщение: {order_data.get('message')}"

    data = {"text": f"*С сайта kamamebel.com поступила новая заявка!*\n"
                    f"Имя: {order_data.get('name')}\n"
                    f"Номер: {order_data.get('number')}\n"
                    f"{message}"}
    url = f"https://telepush.dev/api/messages/{recipient_token}"
    try:
        response = requests.post(url, json=data, timeout=EXTERNAL_TIMEOUT)
    except requests.RequestException as e:
        # Без текста исключения: в нём URL с токеном получателя.
        raise RuntimeError(f"telepush request failed: {type(e).__name__}") from None
    if response.status_code >= 400:
        raise RuntimeError(f"telepush returned {response.status_code}")
