from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from . import permissions as mypermissions
from .throttling import *
from .pagination import MyPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(["GET"])
def getuserinfo(request):
    user = JWTAuthentication().authenticate(request)
    seria = UserSerializer(instance=user[0])
    return Response(seria.data, status=status.HTTP_200_OK)


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(methods=["GET"], detail=False)
    def gadetail(self, request):
        serial = CategorySerializer(instance=Category.objects.all()[:3])
        return Response(data=serial.data, status=status.HTTP_200_OK)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListView2(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CategoryDetailView2(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.delete(request, pk)


class CategoryListView1(APIView):
    """
    1 继承Django自带的View类需要些对应的http方法
    2 继承DRF自带的APIview即可完成请求响应的封装，APIview继承封装了Django的View
    """

    # instance 从数据库中提取
    def get(self, request):
        seria = CategorySerializer(instance=Category.objects.all(), many=True)
        return Response(seria.data, status=status.HTTP_200_OK)

    def post(self, request):
        seria = CategorySerializer(data=request.data)
        # if seria.is_valid():
        #     seria.save()
        #     return Response(seria.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data, status=status.HTTP_201_CREATED)


class CategoryDetailView1(APIView):
    def get(self, request, cid):
        seria = CategorySerializer(instance=get_object_or_404(Category, pk=cid))
        return Response(seria.data, status=status.HTTP_200_OK)

    def put(self, request, cid):
        seria = CategorySerializer(instance=get_object_or_404(Category, pk=cid), data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, cid):
        seria = CategorySerializer(instance=get_object_or_404(Category, pk=cid), data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cid):
        seria = get_object_or_404(Category, pk=cid)
        seria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def categoryList(request):
    if request.method == "GET":
        # instance 为需要序列化的对象 来源于数据库
        seria = CategorySerializer(instance=Category.objects.all(), many=True)
        return Response(seria.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        # data 为序列化对象 来源于请求中提取的数据
        seria = CategorySerializer(data=request.data)
        # 从请求中提取的数据序列化前要进行效验
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_201_CREATED)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def categoryDetail(request, cid):
    model = get_object_or_404(Category, pk=cid)
    if request.method == "GET":
        seria = CategorySerializer(model)
        return Response(seria.data, status=status.HTTP_200_OK)
    elif request.method == "PUT" or request.method == "PATCH":
        # 更新就是从请求中提取参数 替换掉从数据库中提取出的数据
        seria = CategorySerializer(instance=model, data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return HttpResponse("当前路由不允许" + request.method + "操作")


class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet 只有拥有GET POST PATCH DELETE 等HTTP动词操作
    queryset 指明 需要操作的模型列表
    serializer_class 指明序列化类
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            return [permissions.IsAdminUser()]
        else:
            return []

    # 局部频次限制类
    # throttle_classes = [MyAnon, MyUser]
    # 局部分页类
    # pagination_class = MyPagination

    # 配置局部搜索
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["name"]
    search_fields = ["name"]


class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class GoodImgViewSets(viewsets.ModelViewSet):
    queryset = GoodImg.objects.all()
    serializer_class = GoodImgSerializer


class UserViewSets(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["POST"], detail=False)
    def regist(self, request):
        seria = UserRegistSerializer(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response("创建成功")


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        if self.action == "update" or self.action == "partial_update" or self.action == "retrieve":
            return [mypermissions.OrderPermission()]
        else:
            return [permissions.IsAdminUser()]
