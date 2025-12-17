from django.shortcuts import render
from core.models import Student

# Create your views here.

def home(request):
    return render(request,'index.html')


def add_student(request):

    if request.method == 'POST':
        Student.object.create(
            student_id = request.POST.get('id')
        )
    return render(request,'student/add_student.html')


def show_student(request):
    return render(request,'student/show_student.html')
