from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Book, Hero


# Create your views here.

def index(request):
    book = Book.objects.all()
    return render(request, 'index.html', {'books': book})


def detail(request, bookid):
    book = Book.objects.get(id=bookid)

    return render(request, 'detail.html', {'books': book})


def about(request):
    return HttpResponse("这里是关于页面")


def deletebook(request, bookid):
    book = Book.objects.get(id=bookid)

    book.delete()
    url = reverse("booktest:index")
    return redirect(to=url)


def deletehero(request, heroid):
    hero = Hero.objects.get(id=heroid)
    bookid = hero.book.id
    hero.delete()
    url = reverse("booktest:detail", args=(bookid,))
    return redirect(to=url)


def createdbook(request, bookid):
    if request.method == "GET":
        return render(request, 'createdbook.html')
    elif request.method == "POST":
        hero = Hero()
        hero.name = request.POST.get("heroname")
        hero.conten = request.POST.get("heroconten")
        hero.gender = request.POST.get("sex")
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse("booktest:detail", args=(bookid,))
        return redirect(to=url)


def etidhero(request, heroid):
    hero = Hero.objects.get(id=heroid)
    if request.method == "GET":
        return render(request, 'etidhero.html', {"hero": hero})
    elif request.method == "POST":
        hero.name = request.POST.get("heroname")
        hero.conten = request.POST.get("heroconten")
        hero.gender = request.POST.get("sex")
        hero.save()
        url = reverse("booktest:detail", args=(hero.book.id,))
        return redirect(to=url)
