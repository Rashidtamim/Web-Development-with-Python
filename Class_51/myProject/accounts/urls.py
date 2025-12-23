from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage,),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_logout/', views.user_logout, name='user_logout'),

    path('add_student/',views.add_student,name='addstudent'),
    path('all_student/',views.all_student,name='all_student'),
    path('delete_student/<int:id>', views.delete_student,name='delete_student'),
    path('view_student/<int:id>', views.view_student,name='view_student'),
    path('edit_student/<int:id>', views.edit_student,name='edit_student'),
]