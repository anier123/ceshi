from django.conf.urls import url
from . import views

app_name = "polls"
urlpatterns = [
    url(r'^polls/$', views.polls, name="polls"),
    url(r'^detail1/(\d+)/$', views.detail1, name="detail1"),
    url(r'^result/(\d+)$', views.result, name="result")
]