"""
URL configuration for jinja project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jinja.views import form,table,jinja_filter

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='table/',view=table,name='table'),
    path(route='form/',view=form, name='form'),
    path(route='jinja_filter/',view=jinja_filter, name='jinja_filter'),
]
