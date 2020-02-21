from django.contrib.syndication.views import Feed
from django.shortcuts import reverse
from .models import *


class ArticleFeed(Feed):
    title = "web全栈开发技术"
    description = "定期发布一系列web全栈开发技术"
    link = "/"

    def items(self):
        return Article.objects.all().order_by("-create_time")[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.name

    def item_link(self, item):
        url = reverse("blogapp:detail", args=(item.id,))
        return url
