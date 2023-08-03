from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View # import working for only this class
from .models import *
from django.http import HttpResponse
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


# def contact(req):
#     contact = Contact.objects.all()
#     branche = Branche.objects.all()
#     context = {
#         "contact": contact,
#         "branche": branche,
#     }
#     return render(req, "pages/contact.html", context) 

# class ContactView(TemplateView):
#     template_name = 'pages/contact.html'
    
    # It's not working!
    # def render_data(self, **kwargs):
    #     context = super(ContactView, self).get_context_data(self,**kwargs)
    #     context['contact'] = Contact.objects.all()
    #     context['branche'] = Branche.objects.all()
    #     return context
    
class ContactView(View):
    def get(self, request):
        return HttpResponse("result")