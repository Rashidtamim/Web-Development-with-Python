from django.shortcuts import redirect, render

from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'index.html')


def register(request):
    
    if request.method == "POST":
        User.objects.create_user(
            username = request.POST.get('username'),
            password = request.POST.get('password')
        )
        
        return redirect('user_login')
        
    
    return render(request, 'auth/registration.html')


def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        
        if user:
            login(request, user)
            
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('dashboard')
        else:
            return HttpResponse("Invalid Username or Password!!!")
    
    return render(request, 'auth/login.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')
    
@login_required
def dashboard(request):
    
    return render(request, 'dashboard.html')