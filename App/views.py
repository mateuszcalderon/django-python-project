from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Function to render the home page
def home(request):
    return render(request, 'home.html')

# Function to render the user creation page
def create(request):
    return render(request, 'create.html')

# Function to handle user registration and validation
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-confirmation']):
        data['msg'] = 'Password and Password Corfirmation are different.'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user-name'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['first-name']
        user.save()
        user.user_permissions.add(16)
        data['msg'] = 'Success!'
        data['class'] = 'alert-success'
    return render(request, 'create.html', data)

# Function to render the login page
def painel(request):
    return render(request, 'painel.html')

# Function to handle user authentication and login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user-name'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'User Name or Password is wrong.'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)

# Function to render the user dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')

# Function to handle user logout
def logouts(request):
    logout(request)
    return  redirect('/painel/')
