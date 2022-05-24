from django.shortcuts import render, redirect
from .models import Student, Faculty

# Create your views here.
def homepage(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'all_students' : students})

def facdata(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculty.html', {'all_faculty' : faculties})

def update(request):
    posts =[1, 2, 3, 4, 5, 6, 7]
    return render(request, 'update.html', {'posts' : posts})


def post (request, pk):
    return render (request, 'post.html', {'post_number' : pk})

def delete(request):
    return render(request, 'delete.html')

def addFac(request):
    if request.method == "POST":
        name = request.POST.get('name')
        qual = request.POST.get('qualification')
        sal = request.POST.get('salary')

        # print(name, sal, qual)
        fac = Faculty(faculty_name=name, qualification=qual, salary=sal)
        fac.save()

        return redirect("faculty")

    return render(request, 'add-faculty-form.html')

def addStudent(request):
    if request.method == 'POST':
        entered_name = request.POST['name']
        entered_age = request.POST['age']
        entered_address = request.POST['address']

        s = Student(student_name=entered_name, age=entered_age, address=entered_address)
        s.save()

        return redirect("homepage")

    return render (request, 'add-student.html')

def display(request):
    if request.method == "POST":
        fac_name = request.POST['name']
        fac_qualification = request.POST['qualification']
        fac_salary = request.POST['salary']
        print(fac_name, fac_qualification, fac_salary)

        context = {
            'name' : fac_name, 
            'qualification' : fac_qualification,
            'salary' : fac_salary
        }

        return render(request, 'display.html', context)
    else:
        return render(request, 'display.html')