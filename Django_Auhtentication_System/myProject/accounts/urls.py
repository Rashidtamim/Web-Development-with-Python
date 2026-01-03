from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.user_login,name='log'),
    path('register/',views.user_register,name='reg'),
    path('dashboard/',views.dashboard,name='dash'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('all_profile/',views.all_students,name='all_students'),
]