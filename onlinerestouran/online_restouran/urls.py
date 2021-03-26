from django.urls import path
from .views import *


urlpatterns = [
    path('', CategoryView.as_view()),
]