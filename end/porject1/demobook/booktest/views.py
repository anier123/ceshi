from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book


# Create your views here.

def index(request):
    book = Book.objects.all()
    return render(request, 'index.html', {'books': book})


def detail(request, bookid):
    book = Book.objects.get(id=bookid)

    return render(request, 'detail.html', {'books': book})


def about(request):
    return HttpResponse("这里是关于页面")
