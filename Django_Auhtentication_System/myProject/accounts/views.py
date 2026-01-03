from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,'home.html')

# this is a login section
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username ,password=password)
        

        if user:
            login(request,user)
            return redirect('dash')


    return render(request,'auth/login.html')


#this is logout section
def user_logout(request):
    
    logout(request)
    
    return redirect('log')

#this is user registration section

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
@login_required
def dashboard(request):
    return render(request,'protected/dashboard.html')

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


@login_required
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')

    return render(request, 'student/edit_profile.html')

@login_required
def all_students(request):
    users = User.objects.all()  # get all users
    return render(request, 'student/all_student.html', {'users': users})



