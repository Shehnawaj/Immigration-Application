"""
URL configuration for FD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/',views.Home,name='Home'),
    path('services/',views.services,name='services'),
    path('About_Us/',views.About_Us,name='About_Us'),
    path('Countries/',views.Countries,name='Countries'),
    path('Contact/',views.Contact,name='Contact'),
    path('form/',views.consultant,name='form'),
    path('datasave/',views.datasave,name='datasave'),
    path('data_save/',views.data_save,name='data_save'),
    ## Releted pages##
    path('studyvisa/',views.studyvisa,name='studyvisa'),
    path('touristvisa/',views.touristvisa,name='touristvisa'),
    path('businessvisa/',views.businessvisa,name='businessvisa'),
    path('residence/',views.residence,name="residence"),
    path('familysvisa/',views.familysvisa,name='familysvisa'),
    path("visitorvisa/",views.visitorvisa,name="visitorvisa"),
    ### countries pages #### 
    path('canada/',views.canada,name="canada"),
    path('USA/',views.USA,name="USA"),
    path('United_Kingdom/',views.United_Kingdom,name="United_Kingdom"),
    path('Australia/',views.Australia,name="Australia"),
    path('Europe/',views.Europe,name="Europe"),
    path('Germany/',views.Germany,name="Germany"),
]
