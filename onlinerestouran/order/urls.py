from django.urls import path
from .views import *

urlpatterns = [
    path('order/', OrderView.as_view()),
    path('worker/', WorkerView.as_view())
]
