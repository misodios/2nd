from django.contrib import admin

# Register your models here.
from .models import Student, Course, Image
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Image)

