from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# -------------------------
# Home
# -------------------------

def home(request):
    return render(request, 'home.html')


# -------------------------
# Login (Username or Email)
# -------------------------

def user_login(request):
    if request.method == "POST":
        login_input = request.POST.get('username_email')
        password = request.POST.get('password')


        # Allow login via email or username
        try:
            user_obj = User.objects.get(email=login_input)
            username = user_obj.username

        except User.DoesNotExist:
            username = login_input

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username/email or password.')
            return redirect('login')

    return render(request, 'auth/login.html')


# -------------------------
# Logout
# -------------------------

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


# -------------------------
# Register
# -------------------------

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname', '').strip()
        last_name = request.POST.get('lastname', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password')

        # Validation
        if not all([username, email, password]):
            messages.error(request, 'All fields are required.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.first_name = first_name
        user.last_name = last_name
        user.save()

        messages.success(request, 'Account created successfully. Please login.')
        return redirect('login')

    return render(request, 'auth/register.html')


# -------------------------
# Dashboard
# -------------------------

@login_required
def dashboard(request):
    return render(request, 'protected/dashboard.html')


# -------------------------
# Profile
# -------------------------

@login_required
def profile(request):
    return render(request, 'protected/profile.html')


# -------------------------
# Change Password (Manual)
# -------------------------

@login_required
def change_password(request):
    user = request.user

    if request.method == "POST":
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not all([old_password, new_password, confirm_password]):
            messages.error(request, 'All fields are required.')
            return redirect('change_password')

        if not user.check_password(old_password):
            messages.error(request, 'Old password is incorrect.')
            return redirect('change_password')

        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('change_password')

        if len(new_password) < 6:
            messages.error(request, 'Password must be at least 6 characters.')
            return redirect('change_password')

        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)

        messages.success(request, 'Password changed successfully.')
        return redirect('profile')

    return render(request, 'protected/change_password.html')
