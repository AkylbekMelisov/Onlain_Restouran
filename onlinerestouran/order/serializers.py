from rest_framework import serializers
from .models import *


class MealToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealToOrder
        fields = ['order', 'meal', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    mealtoorder_set = MealToOrderSerializer(many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'total_sum', 'date_create', 'status', 'payment', 'promocode', 'mealtoorder_set', 'total_price']

    def create(self, validated_data):
        mto_data = validated_data.pop('mealtoorder_set')
        order = Order.objects.create(**validated_data)
        for mto in mto_data:
            MealToOrder.objects.create(order=order, **mto)
        return order

    def get_total_price(self, obj):
        total_price = 0
        mto = obj.mealtoorder_set.all()
        for mt in mto:
            total_price += mt.meal.price * mt.quantity
        return total_price


class WorkerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'
