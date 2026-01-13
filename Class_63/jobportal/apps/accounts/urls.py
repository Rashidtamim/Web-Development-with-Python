from django.urls import path
from apps.accounts.views import *

urlpatterns = [
    path('login/',login,name='login'),
    path('register/',register,name='register'),
]
