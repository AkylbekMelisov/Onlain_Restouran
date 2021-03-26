from django.urls import path
from .views import *


urlpatterns = [
    path('', OrderView.as_view())
]