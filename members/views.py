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
# def register_user(request):
#     form = RegisterForm()
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('login')
#             # return redirect('login')
#     return render(request, "registration/register.html", context={"form": form})


# def login_user(request):
#     forms = LoginForm()
#     if request.method == 'POST':
#         forms = LoginForm(request.POST)
#         if forms.is_valid():
#             username = forms.cleaned_data['username']
#             password = forms.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('dashboard')
#     context = {'form': forms}
#     return render(request, 'registration/login.html', context)


# def logout_user(request):
#     logout(request)
#     return redirect('login')

