from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request,'homepage.html')

def works(request):
    return render(request,'info.html')

def projo(request):
    proj = Projects.objects.all()
    return render(request,'projects.html',{'proj':proj})