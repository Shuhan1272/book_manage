from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name 

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 
    
