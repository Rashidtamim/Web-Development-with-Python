from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.homepage,),
    path('register/',views.register, name='register'),
    path('login/',views.user_login,name='user_login'),

]