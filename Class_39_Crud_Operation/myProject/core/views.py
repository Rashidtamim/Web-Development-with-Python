from django.shortcuts import redirect, render

from core.models import Student


# Create your views here.


def home(request):

    return render(request,'index.html')

def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
         student_id =int(request.POST.get('student_id')),
         full_name = request.POST.get('full_name'),
         department = request.POST.get('department'),
         dob = request.POST.get('dob'),
         gender = request.POST.get('gender'),
         address = request.POST.get('address'),
        )
        redirect('all_student')
    return render(request,'student/add_student.html')

def all_student(request):
    students = Student.objects.all()
    context = {
        'students': students
    }

    return render(request,'student/all_student.html',context)


def view_student(request, id):
    student = Student.objects.filter(id=id)
    context = {
        'student': student
    }
    return render(request, 'student/view_student.html', context)

def delete_student(request, id):
    student = Student.objects.filter(id=id)
    student.delete()
    
    return redirect('all_student')
