from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class CategoryDetailSerializer(serializers.ModelSerializer):
    meal_set = MealSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'meal_set']

