from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("Hello ")

def homePage(request):

    context = {
        'title' : 'HomePage' ,
        'message' : 'Welcome to Django'

    }
    return render(request,'index.html',context)
    # return render(request,'index.html')
