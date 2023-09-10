from django.http import JsonResponse
from .models import (
    Question,
    Review,
    PopularModel
)
from .serializers import (
    QuestionSerializer,
    ReviewSerializer,
    PopularModelSerializer,
    OrderSerializer
)
from rest_framework import status
from rest_framework.decorators import api_view


def aggregate_data(request):
    try:
        questions = Question.objects.all()
        reviews = Review.objects.select_related('sofa').all()
        popular_models = PopularModel.objects.select_related('sofa').all()

        questions_data = QuestionSerializer(questions, many=True).data
        reviews_data = ReviewSerializer(reviews, many=True).data
        popular_models_data = PopularModelSerializer(popular_models, many=True).data

        aggregated_data = {
            'questions': questions_data,
            'reviews': reviews_data,
            'popular_models': popular_models_data
        }

        return JsonResponse(aggregated_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@api_view(['POST'])
def create_order(request):
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
