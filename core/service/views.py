from django.http import JsonResponse, HttpResponse
from .models import Question, Review, PopularModel, ReviewPhoto
from .serializers import (
    QuestionSerializer,
    ReviewSerializer,
    PopularModelSerializer,
    OrderSerializer,
)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.core.files.storage import default_storage

import os
import hmac
import hashlib
import json
import requests
from django.conf import settings


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

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def get_reviews(request):
    try:
        reviews = Review.objects.select_related("sofa").filter(published=True)

        reviews_data = ReviewSerializer(reviews, many=True).data

        aggregated_data = {
            "reviews": reviews_data,
        }

        return JsonResponse(aggregated_data, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@api_view(["POST"])
@permission_classes((AllowAny,))
def create_review(request):
    try:
        author = request.POST.get("author")
        review = request.POST.get("review")
        new_review = Review.objects.create(
            author=author,
            review=review,
            published=False,
        )
        photo_files = request.FILES.getlist("photos")
        for i, f in enumerate(photo_files):
            path = default_storage.save("core/service/reviews/" + f.name, f)
            ReviewPhoto.objects.create(field=new_review, photo=path, order=i + 1)

        serializer = ReviewSerializer(new_review)

        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


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

    serializer = OrderSerializer(data=request.data['request'])
    if serializer.is_valid():
        serializer.save()
        order_data = serializer.data

        bitrix_data = {
            "fields[TITLE]": f"{order_data.get('name')} - kamamebel.com",
            "fields[NAME]": order_data.get("name"),
            "fields[PHONE][0][VALUE]": order_data.get("number"),
            "fields[SOURCE_ID]": "WEB",
            "fields[COMMENTS]": f'Клиент оставил сообщение "{order_data.get("message")}"' if order_data.get("message") else 'Клиент не оставил сообщения',
            "fields[ASSIGNED_BY_ID]": "1",
            "fields[OPENED]": "Y",
        }

        params_str = "&".join(f"{key}={value}" for key, value in bitrix_data.items())
        bitrix_webhook_url = f"{settings.BITRIX_WEBHOOK_URL}/crm.lead.add.json"
        response = requests.post(f'{bitrix_webhook_url}?{params_str}')
        
        if response.status_code == 200:
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(
                {"error": "Failed to send data to Bitrix24"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
