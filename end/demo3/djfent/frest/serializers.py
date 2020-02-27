from rest_framework import serializers
from .models import *


class CustomSerializer(serializers.RelatedField):
    """
    自定义序列化
    """

    def to_representation(self, value):
        """
        重写字段的输出格式
        :param value:
        :return:
        """
        return str(value.id) + "--" + value.name + "--" + value.desc


class CategorySerializer(serializers.Serializer):
    """
    序列化类 决定了模型序列化细节
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, min_length=3, error_messages={
        "max_length": "长度过长",
        "min_length": "长度过短"
    })

    def create(self, validated_data):
        """
        重写create 定义模型创建方法
        :param validated_data:
        :return:
        """
        instance = Category.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        """
        重写update方法， 来定义模型更新方法
        instance.name = validated_data.get("name", instance.name（必须写，如果没有新的name，则还是原来的）)
        :param instance: 更改前实例
        :param validated_data: 更改参数
        :return: 返回新实例
        """
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class CategorySerializer1(serializers.ModelSerializer):
    """
    编写针对Category的序列化类
    本类指明了Category的序列化细节
    需要继承ModelSerializer 才可以针对模型进行序列化
    在Mate类中，model指明序列化的模型 fields指明序列化的字段
    """
    # StringRelatedField() 可以显示关联模型中的__str__返回值， many=True 代表多个对象， read_only=True 代表只读
    # 经常用
    goods = serializers.StringRelatedField(many=True, read_only=True)

    # PrimaryKeyRelatedField显示主键值
    # goods =serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # 显示资源RestFulAPI
    # goods = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='good-detail')

    # 使用自定义序列化
    # goos = CustomSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"


class GoodImgSerializer(serializers.Serializer):
    img = serializers.ImageField()
    good = serializers.CharField(source="good.name")

    def validate(self, attrs):
        print("原始的", attrs)
        try:
            c = Good.objects.get(name=attrs["good"]["name"])
        except:
            raise serializers.ValidationError("输入有误")
        attrs["good"] = c
        print(attrs)
        return attrs

    def create(self, validated_data):
        print("现在的", validated_data)
        instance = GoodImg.objects.create(**validated_data)
        return instance


class GoodSerializer1(serializers.ModelSerializer):
    # 在序列化时指定字段， 再多方 使用source= 模型名.字段名， read_only=Ture 标识不能改
    # category = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Good
        fields = ("name", "desc", "category")


class GoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, min_length=3, error_messages={
        "max_length": "长度过长",
        "min_length": "长度过短"
    })
    category = CategorySerializer(label="分类")

    # validate_category用来添加条件的，区分超级管理员和普通管理员权限
    # validate_  下划线后的必须是外键名，参数名也必须是外键名
    def validate_category(self, category):
        try:
            Category.objects.get(name=category["name"])
        except:
            raise serializers.ValidationError("不存在这个分类")
        return category

    # validate这个方法用来处理接收的数据
    def validate(self, attrs):
        print("现在的", attrs)
        try:
            c = Category.objects.get(name=attrs["category"]["name"])
        except:
            c = Category.objects.create(name=attrs["category"]["name"])
        attrs["category"] = c
        return attrs

    def create(self, validated_data):
        print("good参数", validated_data)
        instance = Good.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance
