from django.contrib import admin
from .models import (
    Question,
    Review,
    ReviewPhoto
)
from django.utils.html import mark_safe


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


admin.register(ReviewPhoto)


class ReviewPhotoInline(admin.TabularInline):  # admin.StackedInline
    model = ReviewPhoto
    extra = 1

    def thumbnail(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100" />')
        return "Предпросмотр пока недоступен, сохраните отзыв для отображения фото."

    thumbnail.short_description = "Предпросмотр фото"
    readonly_fields = ['thumbnail']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    inlines = [ReviewPhotoInline]

    def thumbnail(self, obj):
        if obj.author_photo:
            return mark_safe(f'<img src="{obj.author_photo.url}" width="100" />')
        return "Предпросмотр пока недоступен, сохраните отзыв для отображения фото."

    thumbnail.short_description = "Предпросмотр фото автора"
    list_display = ['author', 'thumbnail']
    readonly_fields = ['thumbnail']
