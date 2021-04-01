from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class CategoryView(APIView):
    def get(self,request, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class MealView(APIView):
    def get(self,request,*args,**kwargs):
        category = Category.objects.get(id=kwargs['category_id'])
        serializer = CategoryDetailSerializer(category, many=True)
        return Response(serializer.data)


