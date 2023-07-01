from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import *
# Create your views here.
# User Sign up
def user_register(request):
    if request.user.is_authenticated:
        return redirect('shop-list')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

# User Login
def user_login(request):
    if request.user.is_authenticated:
        return redirect('shop-list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('shop-list')
        context = {}
        return render(request, 'users/login.html', context)

# User Logout
def user_logout(request):
    logout(request)
    return redirect('shop-list')

def user_profile(request, pk):
    user = User.objects.get(id=pk)
    context = {
        'user': user
    }
    return render(request, 'users/profile.html', context)
