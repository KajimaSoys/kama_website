from django.contrib import admin
from .models import (
    HeaderBlock,
    MainBlock,
    CatalogTeaserBlock,
    PopularModelsBlock,
    AdvantageBlock,
    WhyBlock,
    RequestBlock,
    StagesBlock,
    DeliveryBlock,
    SolutionsBlock,
    ReviewsBlock,
    QuestionsBlock,
    AddQuestionBlock,
    ContactsBlock
)


@admin.register(HeaderBlock)
class HeaderBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(MainBlock)
class MainBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(CatalogTeaserBlock)
class CatalogTeaserBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(PopularModelsBlock)
class PopularModelsBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvantageBlock)
class AdvantageBlockAdmin(admin.ModelAdmin):
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


@admin.register(SolutionsBlock)
class SolutionsBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(ReviewsBlock)
class ReviewsBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(QuestionsBlock)
class QuestionsBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(AddQuestionBlock)
class AddQuestionBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactsBlock)
class ContactsBlockAdmin(admin.ModelAdmin):
    pass







