
from django.contrib import admin

# Register your models here.

from .models import Student
# admin.site.register(Student)
@admin.register(Student)   #decorator
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id','name','email','age','gender','course','image')
    search_fields = ('student_id','name')
    list_filter = ('student_id',)