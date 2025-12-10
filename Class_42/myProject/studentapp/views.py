from django.shortcuts import redirect, render

from studentapp.models import Student

# Create your views here.
def homepage(request):
    return render(request,"index.html",)


def add_student(request):


    if request.method == 'POST':
        Student.objects.create(
        name = request.POST.get('name'),
        student_id = request.POST.get('student_id'),
        email = request.POST.get('email'),
        image = request.FILES.get('image')
        )
        return redirect('show_student')
    return render(request,"student/add_student.html",)



def show_student(request):
    
    data = Student.objects.all()
    
    context = {
        "students": data
    }
    
    return render(request, 'student/show_student.html', context)
