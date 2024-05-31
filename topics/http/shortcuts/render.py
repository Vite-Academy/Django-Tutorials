from django.shortcuts import render

# Create your views here.

def base(request):
    context = {'data': 200}
    return render(
        request, 'base.html', 
        context=context, 
        content_type='text/html', 
        status=200, using=None
        )


# This example is equivalent to:

# from django.http import HttpResponse
# from django.template import loader

# def my_view(request):
#     # View code here...
#     t = loader.get_template("base.html")
#     c = {"foo": "bar"}
#     return HttpResponse(t.render(c, request), content_type="application/xhtml+xml")