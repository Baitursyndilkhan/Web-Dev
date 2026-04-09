from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category        # which model to serialize
        fields = '__all__'      # include all fields (id, name)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'      # includes id, name, price, description,
                                # count, is_active, category