from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import EmpSignup,DealerSignup,CustomerSignup

# Create your views here.
def empSignup(request):
    template = loader.get_template('empSignup.html')
    return HttpResponse(template.render({}, request))


def empSigninAction(request):
  
    first_name=request.POST['first_name']
    last_Name=request.POST['last_name']
    gender=request.POST['gender']
    email=request.POST['email']
    password=request.POST['password']
    EmpSignup(first_name=first_name,last_name=last_Name,gender=gender,email=email,password=password).save()    
    return HttpResponseRedirect(reverse('empSignup'))

def dealerSignup(request):
    template = loader.get_template('dealerSignup.html')
    return HttpResponse(template.render({}, request))


def dealerSigninAction(request):
    obj = DealerSignup.objects.count()
    first_name=request.POST['first_name']
    last_Name=request.POST['last_name']
    gender=request.POST['gender']
    gst=request.POST['gst']
    email=request.POST['email']
    password=request.POST['password']
    location=request.POST['location']
    dealer_id="DEL"+location[:3:]+'/'+str(obj)

    DealerSignup(dealer_id=dealer_id,first_name=first_name,last_name=last_Name,gender=gender,email=email,password=password,location=location,gst=gst).save()    
    return HttpResponseRedirect(reverse('dealerSignup'))

def customerSignup(request):
    template = loader.get_template('customerSignup.html')
    return HttpResponse(template.render({}, request))


def customerSignupAction(request):
    obj = CustomerSignup.objects.count()
    first_name=request.POST['first_name']
    last_Name=request.POST['last_name']
    gender=request.POST['gender']
    phone_number=request.POST['phone_number']
    email=request.POST['email']
    password=request.POST['password']
    location=request.POST['location']
    customer_id="CST"+"/"+location[:3:]+'/'+str(obj)

    CustomerSignup(customer_id=customer_id,first_name=first_name,last_name=last_Name,gender=gender,email=email,password=password,location=location,phone_number=phone_number).save()    
    return HttpResponseRedirect(reverse('dealerSignup'))





