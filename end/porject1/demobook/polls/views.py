from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as lin, logout as lon

# Create your views here.
from .models import Vote, Option, User
from django.views.generic import View, TemplateView, ListView, DetailView, UpdateView, CreateView


def polls(request):
    message = Vote.objects.all()
    return render(request, 'index1.html', {'message': message})


class IndexView(ListView):
    # 方法一、继承的TemplateView
    # template_name = "polls/index.html"
    # def get_context_data(self, **kwargs):
    #     return {"questions":Question.objects.all()}

    # 方法二、继承ListView
    # template_name指明使用的模板
    template_name = "index1.html"
    # queryset 指明返回的结果列表
    queryset = Vote.objects.all()
    # context_object_name 指明返回字典参数的健
    context_object_name = "message"


def detail1(request, messageid):
    message = Vote.objects.get(id=messageid)
    print("当前用户", request.user.username)
    if request.user and request.user.username != '':
        print("已经登陆过")
        option = Vote.objects.get(id=messageid)
        print("现在的",option)
        if option in request.user.questions.all():
            print("已经投过票", request.user.questions.all())
            url = reverse("polls:result", args=(messageid,))
            return redirect(to=url)
        else:
            return render(request, 'detail1.html', {'message': message})
    else:
        url = reverse("polls:login")+"?next=/detail1/"+messageid+"/"
        return redirect(to=url)


class Detail1View(View):
    def get(self, request, messageid):
        message = Vote.objects.get(id=messageid)
        return render(request, 'detail1.html', {'message': message})


def result(request, messageid):
    message = Vote.objects.get(id=messageid)
    if request.method == "POST":
        optionid = request.POST.get("option")
        option = Option.objects.get(id=optionid)
        option.op_verv = option.op_verv + 1
        option.save()
        request.user.questions.add(Vote.objects.get(id=messageid))
        url = reverse("polls:result", args=(messageid,))
        return redirect(to=url)
    elif request.method == "GET":
        return render(request, 'result.html', {'message': message})


class ResultView(View):

    def post(self, request, messageid):
        optionid = request.POST.get("option")
        option = Option.objects.get(id=optionid)
        option.op_verv = option.op_verv + 1
        option.save()
        url = reverse("polls:result", args=(messageid,))
        return redirect(to=url)

    def get(self, request, messageid):
        message = Vote.objects.get(id=messageid)
        return render(request, 'result.html', {'message': message})


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            lin(request, user)
            next = request.GET.get("next")
            if next:
                url = next
            else:
                url = reverse("polls:polls")
            return redirect(to=url)
        else:
            url = reverse("polls:login")
            return redirect(to=url)


def logout(request):
    lon(request)
    url = reverse("polls:login")
    return redirect(to=url)


def regist(request):
    if request.method == "GET":
        return render(request, "regist.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if User.objects.filter(username=username).count() > 0:
            return HttpResponse("用户名已存在")
        else:
            if password != password2:
                return HttpResponse("密码不一致")
            else:
                User.objects.create_user(username=username, password=password)
                url = reverse("polls:login")
                return redirect(to=url)
