from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name="标签名")

    def __str__(self):
        return self.name


# 分类
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类名")

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    name = models.CharField(max_length=20, verbose_name="作者名")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    views = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    body = UEditorField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name="评论人")
    url = models.URLField(default="http://www.rcc.com", verbose_name="个人主页")
    email = models.EmailField(default="1326729135@qq.com", verbose_name="邮箱")
    num = models.PositiveIntegerField(default=3214, verbose_name="验证码")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="所属文章")

    def __str__(self):
        return self.name


# 留言
class leave(models.Model):
    name = models.CharField(max_length=20, verbose_name="名字")
    url = models.URLField(default="http://www.rcc.com", verbose_name="个人主页")
    email = models.EmailField(default="1326729135@qq.com", verbose_name="邮箱")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="留言时间")
    body = models.CharField(max_length=100, verbose_name="内容")

    def __str__(self):
        return self.name


class Comment1(models.Model):
    name = models.CharField(max_length=20, verbose_name="评论人")
    url = models.URLField(default="http://www.rcc.com", verbose_name="个人主页")
    email = models.EmailField(default="1326729135@qq.com", verbose_name="邮箱")
    num = models.PositiveIntegerField(default=3214, verbose_name="验证码")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    body = models.CharField(max_length=100, verbose_name="内容")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="所属文章")

    def __str__(self):
        return self.name
