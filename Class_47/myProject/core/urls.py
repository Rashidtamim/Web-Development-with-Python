from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,),
    path('add_student/',views.add_student,name='sium'),
    path('show_student/',views.show_student,name='sium1')
]