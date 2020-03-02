from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateCampForm
from .models import Camp

# Create your views here.
def showAllCamps(request):
    camps = Camp.objects.all()
    task = 'Create'
    return render(request, 'camps/all_camps.html', {'camps':camps, 'task':task})

@login_required(login_url='login')
def createCamp(request):
    if request.method == "POST":
        form = CreateCampForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Created Camp Successfully!')
            return redirect('all_camps')
    else:
        form = CreateCampForm()
    return render(request, 'camps/create.html', {'form':form})

def showCamp(request, pk):
    camp = get_object_or_404(Camp, pk=pk)
    if camp:
        return render(request, 'camps/camp.html', {'camp': camp})

def updateCamp(request, pk):
    camp = get_object_or_404(Camp, pk=pk)
    task = 'Update'
    
    form = CreateCampForm(instance=camp)
    
    if request.method == "POST":
        form = CreateCampForm(request.POST, instance=camp)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated camp!')
    else:
        form = CreateCampForm(instance=camp)
    
    return render(request, 'camps/create.html', {'form':form, 'task':task})