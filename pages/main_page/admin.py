from django.contrib import admin
from .models import (
    HeaderBlock,
    MainBlock,
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


@admin.register(WhyBlock)
class WhyBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(RequestBlock)
class RequestBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(StagesBlock)
class StagesBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(DeliveryBlock)
class DeliveryBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactsBlock)
class ContactsBlockAdmin(admin.ModelAdmin):
    pass







