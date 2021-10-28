# from .models import User
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields
from django.forms.models import ALL_FIELDS


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'password',
        ] 
        widgets = { 
            'username': forms.TextInput(attrs={ 'class': 'form-control', 'data-val': 'true', 'data-val-required': 'Please enter your user name'}), 
            'password': forms.TextInput(attrs={ 'class': 'form-control', 'data-val': 'true', 'data-val-required': 'Please enter your password' }), 
        }
        

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        # fields = ['username', 'email', 'password1', 'password2'] 
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'password1', 'password2')
        widgets = { 
            'username': forms.TextInput(attrs={ 'class': 'form-control', 'data-val': 'true', 'data-val-required': 'Please enter your user name'}), 
            'password': forms.TextInput(attrs={ 'class': 'form-control', 'data-val': 'true', 'data-val-required': 'Please enter your password' }), 
        }
                
        