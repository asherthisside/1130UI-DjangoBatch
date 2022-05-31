from django.shortcuts import render, redirect
from .models import Blog
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def blog(request):
    all_blogs = Blog.objects.all()
    return render(request,'index.html', {'blogs' : all_blogs})

@login_required(login_url="login")
def fullblog(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blog.html', {'blog' : blog})

def login(request):
    if request.method == 'POST':
        entered_username = request.POST['username']
        entered_password = request.POST['password']

        user = auth.authenticate(username=entered_username, password=entered_password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            messages.info(request, "Invalid credentials. Please try again")
            return redirect("login")
 
    else: 
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        entered_fname = request.POST['fname']
        entered_lname = request.POST['lname']
        entered_username = request.POST['username']
        entered_email = request.POST['email']
        entered_password = request.POST['password']
        entered_password2 = request.POST['password2']

        if entered_password == entered_password2:
            if User.objects.filter(username=entered_username).exists():
                messages.info(request, "Username already exists")
                return redirect ("signup")

            elif User.objects.filter(email=entered_email).exists():
                messages.info(request, "Email already in use")
                return redirect ("signup")

            else:
                user = User.objects.create_user(username=entered_username, email=entered_email, first_name = entered_fname, last_name = entered_lname, password = entered_password)

                return redirect("login")
        else:
            messages.info(request, "Your Passwords don't match. Try again")
            return redirect("signup")
    else:
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect("login")