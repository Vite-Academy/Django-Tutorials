# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# from django.http import HttpResponse, JsonResponse
from .models import *


def main(req):
    # return HttpResponse("<h1>Home</h1>")
    # return JsonResponse({'text': 'Just rendering some JSON :)'})
    context = {'name': 'Sardor'}
    return render(req, "main.html", context)

def tutorials(req):
    context = {'name': 'Sardor'}
    return render(req, 'tutorials.html', context)