from django.shortcuts import render
from .models import Student, Faculty

# Create your views here.
def homepage(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'all_students' : students})

def facdata(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculty.html', {'all_faculty' : faculties})

def premsir(request):
    fac = Faculty.objects.get(faculty_name = 'Prem sir')
    return render(request, 'prem.html', {'faculty' : fac})

def update(request):
    return render(request, 'update.html')

def delete(request):
    return render(request, 'delete.html')