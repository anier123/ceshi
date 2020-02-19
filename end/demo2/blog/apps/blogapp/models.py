from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

# 轮播图
class Ads(models.Model):
    img = models.ImageField(upload_to="ads", verbose_name="图片")
    desc = models.CharField(max_length=20, null=True, blank=True, verbose_name="图片描述")


# 文章分类表
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类名")


# 标签表
class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name="标签名")


# 文章表
class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name="文章标题")
    name = models.CharField(max_length=20, verbose_name="作者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    uodate_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    views = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    body = UEditorField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    tags = models.ManyToManyField(Tag)


# 评论表
class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name="评论人")
    url = models.URLField(default="http://www.rcc.com", verbose_name="个人主页")
    email = models.EmailField(default="1326729135@qq.com", verbose_name="邮箱")
    body = models.CharField(max_length=500, verbose_name="评论内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="所属文章")
