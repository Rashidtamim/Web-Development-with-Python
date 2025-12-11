from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100,null=True)
    student_id = models.IntegerField(null=True)
    # age = models.IntegerField()
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to='studentapp/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
