from django.http import JsonResponse
from rest_framework.decorators import api_view
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
from .serializers import (
    HeaderBlockSerializer,
    MainBlockSerializer,
    AboutBlockSerializer,
    WhyBlockSerializer,
    RequestBlockSerializer,
    StagesBlockSerializer,
    DeliveryBlockSerializer,
    ContactsBlockSerializer
)


def aggregate_data(request):
    try:
        response_data = {}

        header_block = HeaderBlock.objects.first()
        main_block = MainBlock.objects.first()
        about_block = AboutBlock.objects.first()
        why_block = WhyBlock.objects.first()
        request_block = RequestBlock.objects.first()
        stages_block = StagesBlock.objects.first()
        delivery_block = DeliveryBlock.objects.first()
        contacts_block = ContactsBlock.objects.first()

        if header_block:
            response_data['header_block'] = HeaderBlockSerializer(header_block).data
        if main_block:
            response_data['main_block'] = MainBlockSerializer(main_block).data
        if about_block:
            response_data['about_block'] = AboutBlockSerializer(about_block).data
        if why_block:
            response_data['why_block'] = WhyBlockSerializer(why_block).data
        if request_block:
            response_data['request_block'] = RequestBlockSerializer(request_block).data
        if stages_block:
            response_data['stages_block'] = StagesBlockSerializer(stages_block).data
        if delivery_block:
            response_data['delivery_block'] = DeliveryBlockSerializer(delivery_block).data
        if contacts_block:
            response_data['contacts_block'] = ContactsBlockSerializer(contacts_block).data

        return JsonResponse(response_data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

