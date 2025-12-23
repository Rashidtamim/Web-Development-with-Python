from django.db import models

# Create your models here.

class Student(models.Model):

   student_id = models.IntegerField()
   full_name = models.TextField(max_length=150)
   department = models.TextField(max_length=150)
   dob = models.DateField()
   gender = models.TextField(max_length=50)
   address = models.TextField(max_length=150)

   def __str__(self):
      return f"{self.student_id} - {self.full_name}"
