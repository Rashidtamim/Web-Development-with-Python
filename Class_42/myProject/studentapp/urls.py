
from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.homepage,),
    path('add_student',views.add_student,name='add_student'),
    path('show_student',views.show_student,name='show_student'),
]