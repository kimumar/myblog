from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import  TextInput, EmailInput, FileInput, Select, PasswordInput



class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets ={
        'username': TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        'email': EmailInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }