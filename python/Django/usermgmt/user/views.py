from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def index(request):
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
                return redirect ("/")

            elif User.objects.filter(email=entered_email).exists():
                messages.info(request, "Email already in use")
                return redirect ("/")

            else:
                user = User.objects.create_user(username=entered_username, email=entered_email, first_name = entered_fname, last_name = entered_lname, password = entered_password)

                return redirect("login")
        else:
            messages.info(request, "Your Passwords don't match. Try again")
            return redirect("/")
    else:
        return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        entered_username = request.POST['username']
        entered_password = request.POST['password']
        entered_password2 = request.POST['password2']

        if entered_password == entered_password2:
            user = auth.authenticate(username=entered_username, password=entered_password)

            if user is not None:
                auth.login(request, user)
                return redirect("/dashboard")

            else:
                messages.info(request, "Invalid credentials. Please try again")
                return redirect("login")
        else:
            messages.info(request, "Your Passwords don't match. Try again")
            return redirect("login")
    else: 
        return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')