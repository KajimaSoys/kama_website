from rest_framework import serializers
from .models import (
    DeliveryBlock,
    PaymentBlock
)


class DeliveryBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryBlock
        fields = '__all__'


class PaymentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentBlock
        fields = '__all__'
