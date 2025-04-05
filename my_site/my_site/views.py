from django.http import HttpRequest
from django.shortcuts import render
import random

def home(request):
    return render(request, 'home.html')

def log_in(request):
    return render(request, 'log_in.html')

def registration(request):
    return render(request,'registration.html')

