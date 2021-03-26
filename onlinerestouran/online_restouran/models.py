from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)


class Meal(models.Model):
    meal_types = (
        ('vegan', 'vegan'),
        ('no_vegan', 'no_vegan')
    )
    portions = (
        ('1', '1'),
        ('0.7', '0.7')
    )
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    ingredient = models.CharField(max_length=50)
    meal_type = models.CharField(choices=meal_types, max_length=50)
    portion = models.CharField(choices=portions, max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
