from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
import time
from .forms import *
  
# Create your views here. 

# def home_view(request): 
#     context ={} 
#     context['form']= InputForm() 
#     return render(request, "pages/home.html", context)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, "pages/home.html", {'form': form})