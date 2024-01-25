from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"INCORRECT USERNAME OR PASSWORD")
            return redirect('credentials:login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method=='POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        password = request.POST['password']
        cpassword = request.POST['password1']
        email = request.POST['email']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username not available")
                return redirect('credentials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect('credentials:register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save();
                return redirect('credentials:login')

        else:
            messages.info(request,"password not matching")
            return redirect('credentials:register')
        return redirect('/')

    return render(request,'register.html')