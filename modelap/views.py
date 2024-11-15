from django.shortcuts import render, get_object_or_404
from .models import Course

# Create your views here.

def index(request):
  courses = Course.objects.all()
  return render(request,'index.html',{'courses':courses})

def content(request,id):
  course = get_object_or_404(Course,pk=id)
  return render(request,'content.html',{'course':course})


