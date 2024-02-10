from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import *
  
# Create your views here. 

def home_view(request): 
    context ={} 
    context['form']= InputForm() 
    return render(request, "pages/home.html", context)