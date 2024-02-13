from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

# home
def home(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'store/index.html', context)

# about
def about(request):
    return render(request, 'store/about.html')

# login
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in.'))
            return redirect('home')
        else:
            messages.success(request, ('There was an error, please try again'))
            return redirect('login')

    else:    
        return render(request, 'store/login.html')

# logout
def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect('home')

# register
def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have successfully registered'))
            return redirect('home')
        else:
             messages.success(request, ('Whoops there was a problem, please try agaib'))
             return redirect('register')


    else:
        context = {
            'form': form,
        }
        return render(request, 'store/register.html', context)