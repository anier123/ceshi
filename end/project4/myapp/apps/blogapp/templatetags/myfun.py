from django.template import Library
from ..models import *

register = Library()


@register.simple_tag
def get_tag():
    return Tag.objects.all().order_by("-id")


@register.simple_tag()
def get_article(num=3):
    dates = Article.objects.all()[:num]
    return dates


@register.simple_tag()
def get_leave(num=5):
    return leave.objects.all().order_by("-id")[:num]


