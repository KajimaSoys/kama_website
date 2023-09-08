from django.contrib import admin
from .models import (
    DeliveryBlock,
    PaymentBlock
)


@admin.register(DeliveryBlock)
class ModelNameAdmin(admin.ModelAdmin):
    pass


@admin.register(PaymentBlock)
class ModelNameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
           'fields': [
               'title_main',
               'image'
           ]
        }),
        ('Пункт №1', {
            'fields': [
                'title_first',
                'description_first',
                'payment_first'
            ],
        }),
        ('Пункт №2', {
            'fields': [
                'title_second',
                'description_second',
                'payment_second'
            ],
        }),
    ]
