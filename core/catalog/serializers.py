from rest_framework import serializers
from .models import Sofa, SofaImage
from core.service.serializers import ReviewSerializer


class SofaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SofaImage
        fields = ["image"]


class SofaListSerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField()

    def get_first_image(self, obj):
        first_img = obj.images.first()
        return SofaImageSerializer(first_img).data if first_img else None

    class Meta:
        model = Sofa
        fields = [
            "id",
            "name",
            "short_description",
            "price",
            "sofa_form",
            "sofa_type",
            "folding_mechanism",
            "first_image",
            "order",
            "active",
        ]


class SofaDetailSerializer(serializers.ModelSerializer):
    images = SofaImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    other_variants = SofaListSerializer(many=True)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if "other_variants" in ret:
            ret["other_variants"] = [
                variant
                for variant in ret["other_variants"]
                if variant.get("active") == True
            ]
        return ret

    class Meta:
        model = Sofa
        fields = [
            "id",
            "name",
            "description",
            "sofa_form",
            "sofa_type",
            "folding_mechanism",
            "folding_size",
            "height",
            "width",
            "depth",
            "seat_depth",
            "back_height",
            "armrest_height",
            "seat_height",
            "legs_height",
            "straight_module_depth",
            "corner_module_depth",
            "module_depth",
            "pouf_depth",
            "price",
            "images",
            "reviews",
            "other_variants",
            "active",
        ]
