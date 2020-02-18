from django.conf.urls import url
from . import views

app_name = "polls"
urlpatterns = [
    url(r'^polls/$', views.polls, name="polls"),
    # url(r'^polls/$', views.IndexView.as_view(), name="polls"),

    url(r'^detail1/(\d+)/$', views.detail1, name="detail1"),
    # url(r'^detail1/(\d+)/$', views.Detail1View.as_view(), name="detail1"),
    url(r'^result/(\d+)$', views.result, name="result"),
    # url(r'^result/(\d+)$', views.ResultView.as_view(), name="result"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^regist/$', views.regist, name="regist")
]
