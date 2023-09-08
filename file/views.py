from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    # post = Post.objects.all()
    context = {'post': 200}
    return render(request, 'index.html', context=context)