from django.shortcuts import render 

def index(request):
    name = "Deepansh"
    age = 23
    address = "GZB"

    context = {'user_name' : name, 'user_age' : age, 'user_address' : address}
    return render(request, 'index.html', context)