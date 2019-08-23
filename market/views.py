from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms

def homepage(request):
    form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            user = login(request,user)
            products = Product.objects.all()
            return render(request, 'tabela.html', {'products': products}, {'user': user})
        else:    
            return render(request, 'index.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'index.html', {'form': form})


def table(request):
    products = Product.objects.all()
    return render(request, 'tabela.html', {'products': products})
            
            
def logout_user(request):
    logout(request)
    form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = forms.CreateUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('table')
    else:
        form = forms.CreateUser()
    return render(request, 'cadastro.html', {'form': form})


@login_required()
def create_product(request):
    form = forms.NewProduct()
    if request.method == 'POST':
        form = forms.NewProduct(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('table')
    return render(request, 'new_product.html', {'form': form})


@login_required()
def product_detail(request, name):
    product = Product.objects.get(name=name)
    return render(request, 'edit_product.html', {'product': product})

