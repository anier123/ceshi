from django.conf.urls import url
from . import views
from django.urls import include

app_name = "blogapp"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^detail/(\d+)/$', views.detail, name="detail"),
    url(r'^tags/$', views.tags, name="tags"),
    url(r'^langure/$', views.langure, name="langure"),
]