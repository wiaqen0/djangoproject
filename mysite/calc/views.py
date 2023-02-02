from django.shortcuts import render
from .models import food

def home(request):
    return render(request, 'home.html')