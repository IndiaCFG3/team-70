from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from main.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def Login(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        context = {}
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.info(request,"Username or Password Incorrect!")
                return render(request,'forms/login.html',context)

        return render(request,'forms/login.html',context)


def Register(request):
    if request.user.is_authenticated:
        return redirect('Home')
    
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,user + "  Your account has been created successfully! ")

                return redirect('Login')


        context = {'form':form}
        return render(request,'forms/register.html',context)

@login_required(login_url='Login')
def Home(request):
    user = request.user.username

    context = {'user':user}
    return render(request,'forms/home.html',context)

def Logout(request):
    logout(request)
    return redirect('Login')