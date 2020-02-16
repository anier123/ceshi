from django.db import models


# Create your models here.


class Vote(models.Model):
    message = models.CharField(max_length=20, verbose_name="投票问题")


class Option(models.Model):
    content = models.CharField(max_length=20, default=0)
    op_verv = models.IntegerField(max_length=5, default=0)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)

class Option1(models.Model):
    content = models.CharField(max_length=20, default=0)
    op_verv = models.IntegerField(max_length=5, default=0)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
