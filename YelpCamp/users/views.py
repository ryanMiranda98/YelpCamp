from django.shortcuts import render, redirect, HttpResponse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Profile
from django.contrib.auth.models import User

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


def about(request):
    return render(request, 'users/about.html')

def profile(request, pk):
    if request.user.id == pk:
        if request.method == "POST":
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, "Your profile has been updated!")
                return redirect('profile', pk=pk)
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

        return render(request, 'users/profile.html', {'u_form': u_form, 'p_form': p_form})
    else:
        return HttpResponse("Invalid Page")