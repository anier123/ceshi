"""djfent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .settings import MEDIA_ROOT
from django.views.static import serve
from django.conf.urls import url
from frest.views import *
# 引入DRF自带的路由
from rest_framework.documentation import include_docs_urls

# 引入DRF自带的路由类
from rest_framework import routers
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

router = routers.DefaultRouter()

# 可以通过router默认路由注册资源
router.register('categorys', CategoryViewSets)
router.register('goods', GoodViewSets)
router.register('goodimgs', GoodImgViewSets)
router.register('users', UserViewSets)
router.register('orders', OrderViewSets)

urlpatterns = [
    path('admin/', admin.site.urls),
    # 配置RestFulAPI
    path('api/v1', include(router.urls)),

    # 先通过用户名密码  获得token VUE得到refersh以及access保存  通过access请求服务器 通过refresh获得新的access
    url(r'^obtaintoken/$', token_obtain_pair, name="obtaintoken"),
    url(r'^refresh/$', token_refresh, name="refresh"),
    url(r'^getuserinfo/$', getuserinfo),


    # API文档地址
    path('api/v1/desc/', include_docs_urls(title="RestFulAPI", description="RestFulAPI v1")),
    # 为了在DRF路由调试界面能够使用用户相关的功能需要引入一下路由

    # 配置图片路由地址
    url('media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),

    # url(r'^categorylist/$', categoryList, name="categorylist"),
    # url(r'^categorydetail/(\d+)$', categoryDetail, name="categorydetail"),
    # url(r'^categorylist/$', CategoryListView.as_view(), name="categorylist"),
    # url(r'^categorydetail/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name="categorydetail"),
    path('', include('rest_framework.urls'))
]
