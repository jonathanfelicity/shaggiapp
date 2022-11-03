from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required



def isAuthenticated(req):
    if req.user.is_authenticated:
        return redirect('dashboard')


def login(req):
    isAuthenticated(req)
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(req, user)
            return redirect('/dashboard')

        else:
            return redirect('/login')

    return render(req, 'login.html')


def signup(req):
    isAuthenticated(req)
    if req.method == 'POST':
        sign = req.POST
        user = User.objects.create_user(
            username=sign['username'], 
            email=sign['username'], 
            password=sign['username']
        )
        user.save()
        return redirect('login')
    return render(req, 'signup.html')

@login_required
def _logout(req):
    logout(req)
    
@login_required(login_url='/login')
def dashboard(req):
    return render(req, 'accounts/dashboard.html')