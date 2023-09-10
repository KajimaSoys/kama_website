from rest_framework import serializers
from .models import (
    Question,
    Review,
    ReviewPhoto,
    PopularModel,
    Order
)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ReviewPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewPhoto
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    photos = ReviewPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ['author', 'review', 'author_photo', 'order', 'photos']


class PopularModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):

        from core.catalog.serializers import SofaListSerializer

        representation = super().to_representation(instance)
        representation['sofa'] = SofaListSerializer(instance.sofa).data
        return representation

    class Meta:
        model = PopularModel
        fields = ['order', 'sofa']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
