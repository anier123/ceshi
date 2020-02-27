from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类名")

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=20, verbose_name="商品名字")
    desc = models.CharField(max_length=100, null=True, blank=True, verbose_name="商品描述")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类", related_name='goods')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class GoodImg(models.Model):
    img = models.ImageField(upload_to="goodimg", verbose_name="图片")
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name="商品", related_name="imgs")

    def __str__(self):
        return self.good.name
