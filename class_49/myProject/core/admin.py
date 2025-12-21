from django.contrib import admin

from .models import Student
# Register your models here.

# admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','student_id','email','image')
    search_fields = ('name','student_id')
