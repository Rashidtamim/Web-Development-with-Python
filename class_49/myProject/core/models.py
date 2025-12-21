from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    roll_number = models.IntegerField(null=True)
    course = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    image = models.ImageField(upload_to='core/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} {self.email}'