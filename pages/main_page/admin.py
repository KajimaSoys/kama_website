from django.contrib import admin
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


@admin.register(HeaderBlock)
class HeaderBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(MainBlock)
class MainBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(AboutBlock)
class AboutBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(WhyBlock)
class WhyBlockAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Пункт №1', {
            'fields': [
                'title_first',
                'description_first'
            ],
        }),
        ('Пункт №2', {
            'fields': [
                'title_second',
                'description_second'
            ],
        }),
        ('Пункт №3', {
            'fields': [
                'title_third',
                'description_third'
            ],
        }),
        ('Пункт №4', {
            'fields': [
                'title_fourth',
                'description_fourth'
            ],
        }),
        ('Пункт №5', {
            'fields': [
                'title_fifth',
                'description_fifth'
            ],
        }),
        ('Пункт №6', {
            'fields': [
                'title_sixth',
                'description_sixth'
            ],
        }),
    ]


@admin.register(RequestBlock)
class RequestBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(StagesBlock)
class StagesBlockAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Пункт №1', {
            'fields': [
                'title_first',
                'description_first'
            ],
        }),
        ('Пункт №2', {
            'fields': [
                'title_second',
                'description_second'
            ],
        }),
        ('Пункт №3', {
            'fields': [
                'title_third',
                'description_third'
            ],
        }),
        ('Пункт №4', {
            'fields': [
                'title_fourth',
                'description_fourth'
            ],
        }),
        ('Пункт №5', {
            'fields': [
                'title_fifth',
                'description_fifth'
            ],
        }),
        ('Изображения', {
            'fields': [
                'image_first',
                'image_second'
            ],
        }),
    ]


@admin.register(DeliveryBlock)
class DeliveryBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactsBlock)
class ContactsBlockAdmin(admin.ModelAdmin):
    pass







