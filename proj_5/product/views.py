from django.shortcuts import render
from product.models import product_model
from django.http import HttpResponse


# Create your views here.
def create_view(request,name, desc, price, disc=5):
    res = product_model.objects.create(name = name, desc = desc, price = price,discount = disc)
    return HttpResponse("<h1> DATA STORED SUCCESSFULLY .!</h1>")

def insert_view(request):
    res = product_model.objects.all()
    return render(request,template_name='list.html',context={'data':res})

def details_view(request,id):
    res = product_model.objects.filter(id = id)
    return render(request=request,template_name='details.html',context={'data':res})

def delete_view(request,id):
    res = product_model.objects.get(id = id).delete()
    return HttpResponse('<h1> Product is Deleted Successfully .!</h1>')

def update_view(request,id,price):
    res = product_model.objects.filter(id = id).update(price= price)
    return HttpResponse("<h1> Updated Details Successfully.! </h1>")

def details_col(request):
    res = product_model.objects.all()
    return render(request,template_name='list2.html',context={'data':res})

def registration(request):
    return render(request=request,template_name='registration.html')

