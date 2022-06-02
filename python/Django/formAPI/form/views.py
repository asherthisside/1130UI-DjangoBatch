from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            context = {
                'name' : username,
                'pass' : password
            }
            return render(request, 'index.html', context)

    else:
        form = LoginForm()
        return render(request, 'index.html', {'login_form' : form})