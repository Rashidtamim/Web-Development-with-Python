from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.IntegerField()
    # age = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to='studentapp/')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
