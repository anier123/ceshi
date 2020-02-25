from django import forms

from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment1
        fields = ["name", "url", "email", "num", "body"]
        labels = {
            "name": "名字",
            "url": "网址",
            "email": "邮箱",
            "num": "验证码",
            "body": "评论"
        }
        widgets = {
            "body": forms.Textarea
        }


class LeaveForm(forms.ModelForm):
    class Meta:
        model = leave
        fields = ["name", "url", "email", "body"]
        labels = {
            "name": "名字",
            "url": "网址",
            "email": "邮箱",
            "body": "评论"
        }
        widgets = {
            "body": forms.Textarea
        }
