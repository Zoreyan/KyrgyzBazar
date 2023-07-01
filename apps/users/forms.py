from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'name',
                'placeholder': 'Логин',
            }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'type': 'password',
                'placeholder': 'Пароль',
                'for': 'password1'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'type': 'password',
                'placeholder': 'Повторите пароль',
                'for': 'password2'
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']