from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import User

# Create your views here.

def homepage(request):
    return render(request,'index.html')


def register(request):

    if request.method == "POST":
        User.object.create_user(
            username = request.POST.get("username"),
            password = request.POST.get("password"),
        )
        return redirect('user_login')
    return render(request,'auth/register.html')


def user_login(request):
    return render(request,'auth/login.html')






