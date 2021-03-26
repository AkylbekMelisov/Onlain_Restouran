from django.urls import path
from .views import *


urlpatterns = [
    path('', CategoryView.as_view()),
    path('meals/<int:category_id>/', MealView.as_view()),
]