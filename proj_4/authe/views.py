from authe.models import client

from django.shortcuts import render

def index(request):
    return render(request=request,template_name='index.html')

# Create your views here.

def home(request):
    return render(request=request,template_name='home.html')

def registration(request):
    return render(request,template_name='registration.html')


def register_view(request):
    res = client.objects.all()
    return render(request=request,template_name='registration.html',context={'data':res })


# from django.views.generic import ListView
# from authe.models import client

# class clientdata(ListView):
#   model = client
#   template_name = 'registration.html'
