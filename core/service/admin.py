from django.contrib import admin
from .models import (
    Question,
    Review,
    ReviewPhoto,
    PopularModel,
    Order,
)
from django.utils.html import mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin


@admin.register(Question)
class QuestionAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(PopularModel)
class PopularModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('name', 'number', 'message', 'created',)


admin.register(ReviewPhoto)


class ReviewPhotoInline(SortableInlineAdminMixin, admin.TabularInline):  # admin.StackedInline
    model = ReviewPhoto
    extra = 1

    def thumbnail(self, obj):
        if obj.photo:
            return mark_safe(f'<a href="{obj.photo.url}"><img src="{obj.photo.url}" width="200" /></a>')
        return "Предпросмотр пока недоступен, сохраните отзыв для отображения фото."

    thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail']


@admin.register(Review)
class ReviewAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ReviewPhotoInline]

    def thumbnail(self, obj):
        if obj.author_photo:
            return mark_safe(f'<a href="{obj.author_photo.url}"><img src="{obj.author_photo.url}" width="200" /></a>')
        return "Предпросмотр пока недоступен, сохраните отзыв для отображения фото."

    thumbnail.short_description = "Предпросмотр фото автора"
    list_display = ['author', 'thumbnail']
    readonly_fields = ['thumbnail']
