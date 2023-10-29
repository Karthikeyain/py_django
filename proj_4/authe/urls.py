from django.urls import path 
from authe.views import  index,home,registration

urlpatterns= [
    path('index/',view=index, name='index/'),
    path('home/',view=home,name='home'),
    path(route='reg/',view=registration,name='SIGN UP'),
    # path('reg/',clientdata.as_view()),
    # path('cdata/',clientdata.as_view()),
    
]