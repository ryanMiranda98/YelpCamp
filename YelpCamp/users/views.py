from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'users/landing.html')

def registerUser(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if(form.is_valid()):
            form.save()
            messages.success(request, 'User has been successfully registered! Sign in to continue.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})