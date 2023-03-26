from django.shortcuts import render,HttpResponse
from myapp.models import Contact
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')



def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        return HttpResponse('<h1>Form Submitted Successfully</h1>')
    else:
        return render(request,'contact.html')



def services(request):
    return render(request,'services.html')

