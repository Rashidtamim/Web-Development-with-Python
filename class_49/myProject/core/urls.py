from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.homepage,),
    path('add_student/',views.add_student,name='tamim'),
    path('view_student/',views.view_student,name='tamim1'),
    path('edit_student/<int:id>',views.edit_student,name='tamim2'),
   
]