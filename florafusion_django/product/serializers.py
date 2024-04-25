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
            "get_thumbnail",
            "category",
            "name_category"
        )



class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
            "description",
            "get_gategory_image"   
        )
