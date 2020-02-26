from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet 只有拥有GET POST PATCH DELETE 等HTTP动词操作
    queryset 指明 需要操作的模型列表
    serializer_class 指明序列化类
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
