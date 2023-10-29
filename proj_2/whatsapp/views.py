from django.shortcuts import render
from django.http import HttpResponse

def login(request):

    class college:
        name_of_clg = 'pys'

        def __init__(self,name,age,email):
            self.name = name 
            self.age = age
            self.email = email
    return render(request=request,template_name='login.html',context={'clg_name':college('sai',23,'sai@gmail.com'),'a':120,'li':['12','hello','karthikeya','listlastdata'],'di':{'m':'name of data','n': 12345,'x':[12,12,12]}})


def welcome(request):
    return render(request=request,template_name='welcome.html',context={'karthi':'KARTHIKEYA'})


# def home(request):
#     return render(request,'chats.html')

# Create your views here.