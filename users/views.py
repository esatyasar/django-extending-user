from django.shortcuts import render, redirect, HttpResponse
from .forms import UserForm

from django.contrib import auth, messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def register(request):
    form  = UserForm()
    if request.method =='POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request,user)
            return redirect('home')
        
    context = {
        'form_user' : form
    }
    
    return render(request, "users/register.html",context)

def user_logout(request):
    messages.success(request, "You Logout!")
    logout(request)
    return redirect('home')