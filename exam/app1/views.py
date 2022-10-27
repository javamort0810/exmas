from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *

def new(request):
    if request.method == 'POST':
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(username=a, password=b)
        if user == None:
            return redirect('/login/')
        else:
            login(request, user)

    if request.user.is_authenticated:
        data = {
            "news": NEWS.objects.all()
        }
        return render(request, "maqola.html", data)
    else:
        return redirect('/admin/')

def add_news(request):
    a = request.POST.get('sarlavha')
    b = request.POST.get('sana')
    c = request.POST.get('mavzu')
    NEWS.objects.create(sarlavha=a,sana=b,mavzu=c)
    return redirect('/maqola/')


def logout_s(request):
    logout(request)
    return render(request,'login.html')