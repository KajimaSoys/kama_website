from django.contrib import admin
from .models import Sofa, SofaImage
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin


class SofaImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = SofaImage
    extra = 1


class SofaAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = [
        ("Основные характеристики", {'fields': ['name', 'working_name', 'description']}),
        ("Тип, Цвет и Цена", {'fields': ['sofa_type', 'color', 'price']}),
        ("Размеры", {'fields': ['height', 'width', 'depth', 'seat_depth', 'back_height', 'armrest_height']}),
        ("Другие варианты", {'fields': ['other_variants']}),
    ]

    list_display = ['name', 'sofa_type', 'color', 'price']
    inlines = [SofaImageInline]
    # raw_id_fields = ('other_variants',)
    # search_fields = ['name', 'working_name']


admin.site.register(Sofa, SofaAdmin)
