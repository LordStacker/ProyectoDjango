from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):

    return render(request,'mainapp/index.html',{
        'title': 'Intro'
    })

def about(request):

    return render(request,'mainapp/about.html',{
        'title': 'About us'
    })
def register_page(request):

    if request.user.is_authenticated:

        return redirect('/intro')

    else:

        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'You have been registered correctly!!')

                return redirect('/intro')
        
        return render(request, 'users/register.html',{
            'title': 'Register',
            'register_form': register_form
        })
def login_page(request):
    if request.user.is_authenticated:

        return redirect('/intro')

    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/intro')
            else:
                messages.warning(request, 'Failed at login!!')

        return render(request, 'users/login.html',{
            'title': 'Identify'
        })
def logout_user(request):
    logout(request)
    return redirect('login')
