from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "size",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )