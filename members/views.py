from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
# local
from .forms import LoginForm, RegisterForm


# def register(request):
#     context = {}
#     return render(request, 'account/register.html', context)
def login(request):
    context = {}
    return render(request, 'account/login.html', context)
def logout(request):
    context = {}
    return render(request, 'account/logout.html', context)


