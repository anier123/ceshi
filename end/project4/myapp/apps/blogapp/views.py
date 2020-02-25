from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, Page
from .models import *
from .forms import CommentForm, LeaveForm


# Create your views here.


def index(request):
    article = Article.objects.all()

    typepage = request.GET.get("type")
    year = None
    month = None
    category_id = None
    if typepage == "date":
        year = request.GET.get("year")
        month = request.GET.get("month")
        article = Article.objects.filter(create_time__year=year, create_time__month=month).order_by("-create_time")
    elif typepage == "category":
        category_id = request.GET.get("category_id")
        try:
            category = Category.objects.get(id=category_id)
            article = category.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse("分类不合法")
    elif typepage == "tag":
        tag_id = request.GET.get("tag_id")
        try:
            tag = Tag.objects.get(id=tag_id)
            article = tag.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse("标签不合法")
    else:
        article = Article.objects.all()

    paginator = Paginator(article, 2)
    num = request.GET.get("pagenum", 1)
    page = paginator.get_page(num)
    return render(request, 'index.html', locals())


def detail(request, detailid):
    if request.method == "GET":
        try:
            articles = Article.objects.get(id=detailid)
            cf = CommentForm()
            return render(request, 'detail.html', locals())
        except Exception as e:
            return HttpResponse("文章不合法")
    elif request.method == "POST":
        cf = CommentForm(request.POST)
        print(cf,"++++++++++++++++")
        if cf.is_valid():
            print(cf,"+++++++++++++")
            comment = cf.save(commit=False)
            comment.article = Article.objects.get(id=detailid)
            print(comment, "+++++++++++++")
            comment.save()
            print(comment, "------------")
            url = reverse("blogapp:detail", args=(detailid,))
            return redirect(to=url)
        else:
            articles = Article.objects.get(id=detailid)
            cf = CommentForm()
            errors = "输入信息有误"
    return render(request, 'detail.html', locals())


def tags(request):
    article = Article.objects.all()
    return render(request, 'tags.html', locals())


def langure(request):
    if request.method == "GET":
        cf = leave.objects.all()
        return render(request, 'langure.html', locals())
    elif request.method == "POST":
        cf = LeaveForm(request.POST)
        if cf.is_valid():
            cf.save()
            url = reverse("blogapp:langure")
            return redirect(to=url)
    return render(request, 'langure.html', locals())
