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
    fields = ['author', 'review', ]
    extra = 0
    verbose_name = "Отзыв"
    verbose_name_plural = "Отзывы"


@admin.register(Sofa)
class SofaAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = [
        ("Основные характеристики", {'fields': ['name', 'working_name', 'description', 'short_description', 'active']}),
        ("Тип, Цвет и Цена", {'fields': ['sofa_form', 'sofa_type', 'folding_mechanism', 'color', 'price']}),
        ("Размеры", {'fields': ['height', 'width', 'depth', 'seat_depth', 'back_height', 'armrest_height', 'seat_height', 'legs_height']}),
        ("Другие варианты", {'fields': ['other_variants']}),
    ]

    list_display = ['name', 'working_name', 'sofa_form', 'sofa_type', 'folding_mechanism', 'color', 'sizes', 'price', 'thumbnail', 'active']
    list_editable = ['active', ]

    search_fields = ['name', 'working_name', 'color']
    list_filter = ['sofa_form', 'sofa_type', 'folding_mechanism']

    inlines = [SofaImageInline, ReviewInline]
    raw_id_fields = ('other_variants',)
    related_lookup_fields = {
        'fk': ['other_variants'],
    }
    actions = ["copy_selected"]

    def copy_selected(self, request, queryset):
        for obj in queryset:
            obj.working_name += ' - Копия'
            obj.pk = None
            obj.save()

    copy_selected.short_description = "Копировать выбранные объекты"

    def sizes(self, obj):
        return f'{round(obj.height)}*{round(obj.width)}*{round(obj.depth)}мм'

    sizes.short_description = "Размер"

    def thumbnail(self, obj):
        first_image = obj.images.first()
        if first_image and first_image.image:
            return mark_safe(
                f'<a href="{first_image.image.url}"><img src="{first_image.image.url}" width="250" /></a>'
            )
        return "Изображение отсутствует"

    thumbnail.short_description = "Изображение"
