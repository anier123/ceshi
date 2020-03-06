from django.contrib.auth import backends
from django.db.models import Q
from .models import *


class MyLoginBackend(backends.BaseBackend):
    def authenticate(self, request, **kwargs):
        username = kwargs["username"]
        password = kwargs["password"]

        user = User.objects.filter(Q(username=username) | Q(email=username) | Q(telephone=username)).first()
        if user:
            b = user.check_password(password)
            if b:
                return user
            else:
                return None
        else:
            return None
