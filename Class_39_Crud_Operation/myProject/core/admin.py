from django.contrib import admin

# Register your models here.

from .models import Student
# admin.site.register(Student)
@admin.register(Student)   #decorator
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id','full_name','department')
    search_fields = ('student_id','full_name')
    list_filter = ('department',)
