from django.contrib import admin
from .models import Sofa, SofaImage
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.utils.html import mark_safe
from core.service.models import Review


class SofaImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = SofaImage
    extra = 1
    readonly_fields = ['thumbnail']
    fields = ('image', 'thumbnail', 'order')

    def thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<a href="{obj.image.url}"><img src="{obj.image.url}" width="200" /></a>')
        return "Предпросмотр пока недоступен, сохраните товар для отображения фото."

    thumbnail.short_description = "Предпросмотр фото"


class ReviewInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Review
    fields = ['author', 'review',]
    extra = 0
    verbose_name = "Отзыв"
    verbose_name_plural = "Отзывы"


@admin.register(Sofa)
class SofaAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = [
        ("Основные характеристики", {'fields': ['name', 'working_name', 'description']}),
        ("Тип, Цвет и Цена", {'fields': ['sofa_type', 'color', 'price']}),
        ("Размеры", {'fields': ['height', 'width', 'depth', 'seat_depth', 'back_height', 'armrest_height']}),
        ("Другие варианты", {'fields': ['other_variants']}),
    ]

    list_display = ['name', 'sofa_type', 'color', 'price']
    inlines = [SofaImageInline, ReviewInline]
    # raw_id_fields = ('other_variants',)
    # search_fields = ['name', 'working_name']
