'''from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title' : 'Homepage',
        'message' : 'This is django file '
    }
    return render(request,'index.html')'''

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')

def news(request):
    return render(request, 'news.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
