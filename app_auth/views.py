from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm , RegisterForm
from django.forms import ModelForm
from django import forms


def login_blog(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            pwd= form.cleaned_data['pwd']

            user= authenticate(username=username,password=pwd)

            if user is not None:
                login(request,user)  #stocker l'ulisateur dans l'objet request on l'utilise pr savoir si utilisateur est connecté
                return redirect('home')
            else:
                messages.error(request,"authentification échouée")
                return render(request,'login.html',{'form':form})  
        else:
            for field in form.errors:
               

             form[field].field.widget.attrs['class'] += 'is-invalid'

            return render(request,'login.html',{'form':form})  


    else:
        form = LoginForm()
        return render(request,"login.html",{"form":form})


def register(request):
    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            pwd= form.cleaned_data['pwd']

            user = User.objects.create_user(username=username,password=pwd)
            if user is not None:
                return redirect("login-blog")
            else:
                messages.error(request,'création de compte echouée')
                return render(request,'register.html',{"form":form})
        else:
              return render(request,'register.html',{"form":form})      


    


        return render(request,'register.html',{})
        
    form = RegisterForm()

    return render(request,'register.html',{'form':form}) 




