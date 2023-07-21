from django.shortcuts import render
from .models import Contact
# from django.http import HttpResponse
# from django.template import loader

# def home(req):
#     template = loader.get_template('base.html')
#     context = {'data':'result'}
#     return HttpResponse(template.render(context, req))

# -------------------

def home(req):
    return render(req, "pages/home.html")    

def story(req):
    return render(req, "pages/story.html")    

def services(req):
    return render(req, "pages/services.html") 

def price(req):
    return render(req, "pages/price.html") 

def contact(req):
    data = Contact.objects.all()
    context = {"data": data}
    return render(req, "pages/contact.html", context) 