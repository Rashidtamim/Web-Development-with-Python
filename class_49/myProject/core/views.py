from django.shortcuts import render,redirect

from core.models import Student

# Create your views here.

def homepage(request):
    return render(request,'index.html')


def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
        student_id = request.POST.get('studentId'),
        name = request.POST.get('fullName'),
        
        email = request.POST.get('email'),
        roll_number = request.POST.get('rollNumber'),
        course = request.POST.get('course'),
        age = request.POST.get('age'),
        image = request.FILES.get('studentImage')
        )
        return redirect('view_student')
    return render(request,"student/add_student.html",)


    


def view_student(request):

    data = Student.objects.all()
    
    context = {
        "students": data
    }

    
    
    return render(request, 'student/view_student.html', context)

    


