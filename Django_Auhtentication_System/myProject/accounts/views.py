from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,'home.html')


def user_login(request):
    return render(request,'auth/login.html')

def user_register(request):

    if request.method == 'POST':
        user = User.objects.create_user(
            username = request.POST.get('username'),
            email = request.POST.get('email'),
            password = request.POST.get('password'),

        )
        user.first_name = request.POST.get('Firstname')
        user.last_name = request.POST.get('Lastname')

        user.save()
        return redirect('log')

    return render(request,'auth/register.html')

def dashboard(request):
    return render(request,'protected/dashboard.html')