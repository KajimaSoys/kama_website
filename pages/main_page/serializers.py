from rest_framework import serializers
from .models import (
    HeaderBlock,
    MainBlock,
    AboutBlock,
    WhyBlock,
    RequestBlock,
    StagesBlock,
    DeliveryBlock,
    ContactsBlock
)


class HeaderBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderBlock
        fields = '__all__'


class MainBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainBlock
        fields = '__all__'


class AboutBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutBlock
        fields = '__all__'


class WhyBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyBlock
        fields = '__all__'


class RequestBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestBlock
        fields = '__all__'


class StagesBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StagesBlock
        fields = '__all__'


class DeliveryBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryBlock
        fields = '__all__'


class ContactsBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactsBlock
        fields = '__all__'
