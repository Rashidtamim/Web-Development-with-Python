from django.urls import path
from .import views 
from .views import *

urlpatterns = [
    path('',views.index,name='home' ),
    path('news/',views.news,name='news1' ),
    path('about/',views.about,name='about1' ),
    path('contact/',views.contact,name='contact1' ),
]