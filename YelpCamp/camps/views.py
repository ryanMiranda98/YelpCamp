from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showCamps(request):
    return HttpResponse('All camps')