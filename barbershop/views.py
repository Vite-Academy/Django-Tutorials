from django.shortcuts import render
from .models import *
# from django.http import HttpResponse
# from django.template import loader

# def home(req):
#     template = loader.get_template('base.html')
#     context = {'data':'result'}
#     return HttpResponse(template.render(context, req))

# -------------------

def home(req):
    branche = Branche.objects.all()
    context = {
        "branche": branche,
    }
    return render(req, "pages/home.html", context)   
 

def story(req):
    branche = Branche.objects.all()
    context = {
        "branche": branche,
    }
    return render(req, "pages/story.html", context)   
 

def services(req):
    branche = Branche.objects.all()
    context = {
        "branche": branche,
    }
    return render(req, "pages/services.html", context) 


def price(req):
    branche = Branche.objects.all()
    price = Price.objects.all()
    context = {
        "price": price,
        "branche": branche,
    }
    return render(req, "pages/price.html", context) 


def contact(req):
    contact = Contact.objects.all()
    branche = Branche.objects.all()
    context = {
        "contact": contact,
        "branche": branche,
    }
    return render(req, "pages/contact.html", context) 