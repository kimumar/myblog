from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm 
from . decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
# Create your views here.
@unauthenticated_user
def register(request):
    reg = CreateUserForm()
    if request.method == 'POST':
        reg = CreateUserForm(request.POST)
        if reg.is_valid():
            reg.save()
            user = reg.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect('login')
    else:
        messages.warning(request,reg.errors)
        reg = CreateUserForm()

    context = {
        'reg': reg,
    }
    return render(request, 'users/register.html', context)

@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
            messages.error(request, "There Was En error Logging In,  Please Try Again....")
            

    context = {
        
    }
    return render(request, 'users/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')