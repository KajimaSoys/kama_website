from django.http import JsonResponse, HttpResponse
from .models import Question, Review, PopularModel
from .serializers import (
    QuestionSerializer,
    ReviewSerializer,
    PopularModelSerializer,
    OrderSerializer,
)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

import os
import hmac
import hashlib
import json


def aggregate_data(request):
    try:
        questions = Question.objects.all()
        reviews = Review.objects.select_related("sofa").all()
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
        reviews = Review.objects.select_related("sofa").all()

        reviews_data = ReviewSerializer(reviews, many=True).data

        aggregated_data = {
            "reviews": reviews_data,
        }

        return JsonResponse(aggregated_data, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@api_view(["POST"])
@permission_classes((AllowAny,))
def create_order(request):
    hmac_key = os.environ.get("HMAC_KEY", 'asdnjnvksjndfelu')
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
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
