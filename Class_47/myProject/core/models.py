from django.db import models



# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField(null=True)
      
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    age = models.IntegerField()
    gender = models.TextField(max_length=50)
    course = models.CharField(max_length=100,null=True)
    
    image = models.ImageField(upload_to='core/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name