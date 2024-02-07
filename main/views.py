from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def laptops(request):
    return render(request,'main/laptops.html')

def contact(request):
    return render(request,'main/contact.html')

def about(request):
    return render(request,'main/about.html')

def base(request):
    return render(request,'main/base.html')