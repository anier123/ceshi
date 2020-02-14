from django.conf.urls import url
from . import views

app_name = 'booktest'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'detail/(\d+)', views.detail, name='detail'),
    url(r'^about/$', views.about, name='about')
]
