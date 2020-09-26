from django.shortcuts import render
from .models import Tutorial

# Create your views here.








def home(request):
    return render(request,'tutorial/home.html')



