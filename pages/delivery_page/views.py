import logging

from django.http import JsonResponse
from .models import (
    DeliveryBlock,
    PaymentBlock
)
from .serializers import (
    DeliveryBlockSerializer,
    PaymentBlockSerializer
)

from pages.main_page.models import HeaderBlock
from pages.main_page.serializers import HeaderBlockSerializer


logger = logging.getLogger(__name__)


def aggregate_data(request):
    try:
        response_data = {}

        header_block = HeaderBlock.objects.first()
        delivery_block = DeliveryBlock.objects.first()
        payment_block = PaymentBlock.objects.first()

        if header_block:
            response_data["header_block"] = HeaderBlockSerializer(header_block).data
        if delivery_block:
            response_data['delivery_block'] = DeliveryBlockSerializer(delivery_block).data
        if payment_block:
            response_data['payment_block'] = PaymentBlockSerializer(payment_block).data

        return JsonResponse(response_data, safe=False)

    except Exception:
        logger.exception('page data failed')
        return JsonResponse({'error': 'Внутренняя ошибка сервера, попробуйте позже'}, status=500)

