from django.db import models
from online_restouran.models import Meal


class Order(models.Model):
    statuses = (
        ('in_prossec', 'in_prossec'),
        ('ready', 'ready'),
        ('finish', 'finish')
    )
    payment_types = (
        ('cash', 'cash'),
        ('card', 'card')
    )
    total_sum = models.PositiveIntegerField()
    date_create = models.DateTimeField()
    status = models.CharField(choices=statuses, max_length=50, default='in_prossec')
    payment = models.CharField(choices=payment_types, max_length=50, default='cash')
    promocode = models.CharField(max_length=50)


class MealToOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
