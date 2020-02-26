from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    """
    编写针对Category的序列化类
    本类指明了Category的序列化细节
    需要继承ModelSerializer 才可以针对模型进行序列化
    在Mate类中，model指明序列化的模型 fields指明序列化的字段
    """
    # StringRelatedField() 可以显示关联模型中的__str__返回值， many=True 代表多个对象， read_only=True 代表只读
    # 经常用
    goods = serializers.StringRelatedField(many=True, read_only=True)

    # goods =serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # goods = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='good-detail')

    class Meta:
        model = Category
        fields = "__all__"


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = "__all__"
