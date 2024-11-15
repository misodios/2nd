from symtable import Class

from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.email}"

class Course(models.Model):
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    duration = models.CharField(max_length=1)
    #image = models.ImageField(upload_to='images/')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title } {self.department } {self.duration} "


class Image(models.Model):
    uploaded_file = models.FileField(upload_to="images")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.student.email} {self.uploaded_file}"



