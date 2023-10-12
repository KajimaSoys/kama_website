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
    list_display = [
        "get_name",
        "get_working_name",
        "get_sofa_form",
        "get_sofa_type",
        "get_folding_mechanism",
        "get_color",
        "get_sizes",
        "get_price",
        "get_thumbnail",
    ]

    raw_id_fields = ("sofa",)
    related_lookup_fields = {
        "fk": ["sofa"],
    }

    # class Media:
    #     css = {"all": ("admin/css/admin_overrides.css",)}
    #     js = ("admin/js/admin_overrides.js",)

    @admin.display(ordering="sofa__name", description="Название")
    def get_name(self, obj):
        return obj.sofa.name

    @admin.display(description="Рабочее имя")
    def get_working_name(self, obj):
        return obj.sofa.working_name
    
    @admin.display(description="Форма дивана")
    def get_sofa_form(self, obj):
        return obj.sofa.get_sofa_form_display()
    
    @admin.display(description="Тип дивана")
    def get_sofa_type(self, obj):
        return obj.sofa.get_sofa_type_display()
    
    @admin.display(description="Механизм раскладывания")
    def get_folding_mechanism(self, obj):
        return obj.sofa.get_folding_mechanism_display()
    
    @admin.display(description="Цвет")
    def get_color(self, obj):
        return obj.sofa.color
    
    @admin.display(description="Размеры")
    def get_sizes(self, obj):
        return f'{round(obj.sofa.height)}*{round(obj.sofa.width)}*{round(obj.sofa.depth)}мм'

    @admin.display(description="Цена")
    def get_price(self, obj):
        return obj.sofa.price
    
    @admin.display(description="Изображение")
    def get_thumbnail(self, obj):
        first_image = obj.sofa.images.first()
        if first_image and first_image.image:
            return mark_safe(
                f'<a href="{first_image.image.url}"><img src="{first_image.image.url}" width="250" /></a>'
            )
        return "Изображение отсутствует"


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
        return "Предпросмотр недоступен, отсутствует изображение."

    thumbnail.short_description = "Предпросмотр фото автора"
    list_display = ['author', 'thumbnail', 'review', 'published', ]
    list_editable = ['published', ]
    readonly_fields = ['thumbnail']

    raw_id_fields = ("sofa",)
    related_lookup_fields = {
        "fk": ["sofa"],
    }
