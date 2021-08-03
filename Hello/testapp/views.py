from django.shortcuts import render,HttpResponse
from datetime import datetime
from testapp.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    context={"variable":"this is sent"}
    return render(request,'index.html',context)
def about(request):
    return render(request,"about.html")
    #return HttpResponse("about page")
def services(request):
    return render(request,'services.html')
    #return HttpResponse("Services page")
def contacts(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contacts=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contacts.save()
        messages.success(request, 'Your message has been sent.!')
    return render(request,'contacts.html')
    #return HttpResponse("contact page")

