from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from base.models import Userpassword

def login_blog(request):
    
    if request.method == "POST":        
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = authenticate(username=username, password=pwd)
            if user is not None:
                login(request, user)

                return redirect('tasks')
            else:
                messages.error(request, "Les données sont incorrectes")
                return render(request, 'login.html', {'form': form})

        else:

            for field in form.errors:
                form[field].field.widget.attrs['class'] += 'is_invalid'
            return render(request, 'login.html', {'form': form})

    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})



            


def register(request):
    if request.method == "GET":
            form = RegisterForm()
            return render(request, "register.html", {
                'form': form
                })
    else:
            form = RegisterForm(request.POST)
            if  form.is_valid():
                username = request.POST['username']       
                pwd = request.POST['pwd']
                pwd_confirm = request.POST['pwd_confirm']
                if pwd == pwd_confirm:
                    if User.objects.filter(username=username).exists():
                          messages.info(request, 'Ce nom de domaine existe déja')
                          return redirect('register')           
                    else:
                          User.objects.create_user(username=username, password=pwd)
                          Userpassword(username=username,password=pwd).save()                
                          return redirect('login-blog')
                else:
                          messages.error(request, 'Mot de passe incorrect')
                          return redirect('register')               
            else:
                return render(request, 'login.html')

























            


def logout_blog(request):
    logout(request)
    return redirect('login-blog')
            
            



