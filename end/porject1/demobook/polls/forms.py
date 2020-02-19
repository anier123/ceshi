from django import forms
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=16, min_length=3, label="请输入用户名", help_text="最小3个，最大16")
    password = forms.CharField(max_length=12, min_length=6, label="请输入密码", widget=forms.PasswordInput,
                               help_text="最多12，最小6")


class RegistForm(forms.ModelForm):
    password2 = forms.CharField(max_length=12, min_length=6, label="请再次输入密码", widget=forms.PasswordInput,
                                help_text="最多12，最少6")

    class Meta:
        model = User
        fields = ["username", "password"]
        labels = {
            "username": "请输入用户名",
            "password": "请输入密码"
        }
        widgets = {
            "password": forms.PasswordInput
        }
