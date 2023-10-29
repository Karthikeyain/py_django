from django.urls import path 
from product.views import create_view,insert_view,details_view,delete_view,update_view,details_col,registration

urlpatterns  =[
    path('create/<str:name>/<str:desc>/<int:price>/',view=create_view,name='create'),
    path('list/',view=insert_view,name='list'),
    path('details/<int:id>',view=details_view,name='details'),
    path('delete/<id>/',view=delete_view,name='delete'),
    path('update/<id>/<price>/',view=update_view,name='update'),
    path('list2/',view=details_col, name='details in col'),
    path('registration/',view=registration,name='registration'),
]