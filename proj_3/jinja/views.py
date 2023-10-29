from django.shortcuts import render

d ={101: {'name':'karthikeya','email':'@gmailcom'},
    102:{'name':'raja','email':'@gmailcom'},
    103:{'name':'rani','email':'@gmailcom'},
    104:{'name':'jinja','email':'@gmailcom'},
    105:{'name':'dtl','email':'@gmailcom'}}

def form(request):
    return render(request=request,template_name='form.html')

def table(request):
    return render(request=request,template_name='table.html',context={'data':d})

def jinja_filter(request):
    return render(request,'jinja_filter.html',context={'a':'helllo','b': 10, 'l':[10,20,30,100,200]})