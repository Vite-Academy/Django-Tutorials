from django.shortcuts import render

# Create your views here.
def base(request):
    context = {'data': 200}
    return render(request, 'base.html', context=context)