from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fnoo(request):
    return HttpResponse("rahil are you fine")
def fnhome2(request):
    return render(request,'home2.html')   
def fnfb(request):
    return render(request,'fb.html')     

