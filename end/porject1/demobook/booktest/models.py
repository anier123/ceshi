from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateField(default="1998-11-16")
    price = models.FloatField(default=0)


class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default="male")
    conten = models.CharField(max_length=100)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
