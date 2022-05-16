from django.shortcuts import render 

def index(request):
    return render(request, 'index.html')

def my_intro(request):
    return render(request, 'intro.html')