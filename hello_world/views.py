from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Home</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")