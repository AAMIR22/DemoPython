from django.shortcuts import render
from django.utils.functional import empty

from shop.models import Product
from shop.models import Category
from django.db.models import Q
# Create your views here.

def searchresult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query)|Q(description__contains=query)|Q(category__name__contains=query))
    return render(request,'search.html',{'query':query,'products':products})
