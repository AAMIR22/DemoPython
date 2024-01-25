from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import place,offer
# Create your views here.
def demo(request):
    obj = place.objects.all()
    obj1= offer.objects.all()
    return render(request,'index.html',{'result':obj,'result2':obj1})

def about(request):
    return render(request,'about.html')