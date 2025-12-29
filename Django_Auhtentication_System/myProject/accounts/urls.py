from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.user_login,name='log'),
    path('register/',views.user_register,name='reg'),
    path('dashboard/',views.dashboard,name='dash'),
]