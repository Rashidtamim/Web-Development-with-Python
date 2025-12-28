from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout, update_session_auth_hash

from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    
    return render(request, 'home.html')


def user_login(request):
    
    if request.method == "POST":
        login_input = request.POST.get('username_email')
        password = request.POST.get('password')
                
        try:
            user_obj = User.objects.get(email=login_input)
            username = user_obj.username 
            
        except User.DoesNotExist:
            username = login_input
     
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfull!')
            return redirect('dashboard')
        
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
            
    
    return render(request, 'auth/login.html')

def user_logout(request):
    
    logout(request)
    
    return redirect('login')

def register(request):
    
    if request.method == "POST":
        user = User.objects.create_user(
            username = request.POST.get('username'),
            email = request.POST.get('email'),
            password = request.POST.get('password')
        )
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        
        user.save()
        
        return redirect('login')
    
    return render(request, 'auth/register.html')


@login_required
def dashboard(request):
    
    return render(request, 'protected/dashboard.html')

@login_required
def profile(request):
    
    return render(request, 'protected/profile.html')


@login_required
def change_password(request):
    user = request.user 
    
    if request.method == "POST":
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if not user.check_password(old_password):
            messages.error(request, 'Old Password is incorrect!')
            return redirect('change_password')
        
        if new_password != confirm_password:
            messages.error(request, "Passwords are not match!")
            return redirect('change_password')
        
        user.set_password(new_password)
        update_session_auth_hash(request, user)
        
        user.save()
        messages.success(request, 'Password Change Successfully!')
        
        
        return redirect('profile')
        
    return render(request, 'protected/change_password.html')
