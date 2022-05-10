from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def aboutme(request):
    return HttpResponse("<h1>This is about Us Page</h1><p>We are learning Django. Thoda mashup sa ho rha hai</p>") 

def mycontact(request):
    return HttpResponse("<h1>This is the contact page</h1><p>Mujh p ek ehsan krna... ki mujhe contact mt krna ... Please</p>")

def htmlpage(request):
    return render(request, 'index.html')

def header(request):
    return render(request, 'flexheader.html')