"""demobook URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('booktest.urls', namespace='booktest')),
    path('', include('polls.urls', namespace='polls')),

]

# 项目的所有路由地址配置文件
# admin路由哦是django自带的后台管理路由


# 总路由匹配文件 == 项目路由文件 使用include包含应用路由文件

# 硬编码 在html文件中有很多超级链接 其中href属性如果写成聚堆路径 这种就叫硬编码
# 在开发的过程中可能需要反复修改路由 若使用硬编码非常不方便
# 需要解除硬编码
# 1需要给应用一个app_name = "应用名" 下载应用的urls.py中
# 2在项目路由中给应用分流时 在include中  提供命名空间
# 3 在应用中给每一个路由一个名字
# 4 在html中使用时 href = "{% erl '命名空间名:路由name' 如果需要参数 直接写 %}"
# 以前定位路由 靠总路由正则表达+应用路由正则表达式
# 解除硬编码之后 使用 应用命名空间+应用路由名字
