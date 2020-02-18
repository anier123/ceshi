from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    telephone = models.CharField(max_length=20, verbose_name="手机号")
    questions = models.ManyToManyField("Vote")


class Vote(models.Model):
    message = models.CharField(max_length=20, verbose_name="投票问题")


class Option(models.Model):
    content = models.CharField(max_length=20, default=0)
    op_verv = models.IntegerField(default=0)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)

