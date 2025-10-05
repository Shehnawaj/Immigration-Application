from django.shortcuts import render
from .models import Appoint_Consultant , Get_in_touch

# Create your views here.
### GET data by form and save to db
def datasave(request):
    if request.method=='GET':
        name=request.GET.get('name')
        email=request.GET.get('email')
        phone=request.GET.get('phone')
        address=request.GET.get('address')
        appointment=request.GET.get('appointment')
        res = Appoint_Consultant.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            appointment=appointment
        )
        res.save()

    return render(request,'home.html')

def data_save(request):
    if request.method=='GET':
        name=request.GET.get('name')
        email=request.GET.get('email')
        comment=request.GET.get('comment')
        result=Get_in_touch(
            name=name,
            email=email,
            comment=comment
        )
        result.save()
    return render(request,'home.html')
#### viwes for web pages 
def Home(request):
    return render(request,'home.html')
def services(request):
    return render(request,"servies.html")

def About_Us(request):
    return render (request,'About_Us.html')

def Countries(request):
    return render (request,'countries.html')

def Contact(request):
    return render (request,'Contact.html')

def consultant(request):
    return render(request,'consultant.html')
#### Releted pages Create
def studyvisa(request):
    return render(request,'SV.html')

def touristvisa(request):
    return render(request,'TV.html')

def businessvisa(request):
    return render(request,"BS.html")

def residence(request):
    return render(request,"PR.html")

def familysvisa(request):
    return render(request,"FV.html")

def visitorvisa(request):
    return render(request,"VV.html")

## countries function ###

def canada(request):
    return render(request,"canada.html")
def USA(request):
    return render(request,"USA.html")
def United_Kingdom(request):
    return render(request,"United_Kingdom.html")
def Australia(request):
    return render(request,"Australia.html")
def Europe(request):
    return render(request,"Europe.html")
def Germany(request):
    return render(request,"Germany.html")