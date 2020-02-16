from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

# Create your views here.
from .models import Vote,Option


def polls(request):
    message = Vote.objects.all()
    return render(request, 'index1.html', {'message': message})


def detail1(request, messageid):
    message = Vote.objects.get(id=messageid)
    return render(request, 'detail1.html', {'message': message})


def result(request, messageid):
    message = Vote.objects.get(id=messageid)
    if request.method == "POST":
        optionid = request.POST.get("option")
        option = Option.objects.get(id=optionid)
        option.op_verv = option.op_verv + 1
        option.save()
        url = reverse("polls:result", args=(messageid,))
        return redirect(to=url)
    elif request.method == "GET":
        return render(request, 'result.html', {'message': message})
