"""
Views module for the application.

This module contains the view functions that handle HTTP requests and returns responses.
Each view corresponds to a specific URL pattern.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Message

def login_view(request):
    """
    Handle user login functionality.

    Args:
        request: HttpRequest object containing user credentials

    Returns:
        HttpResponse: Redirects to home page on successful login,
                     or renders login form with error message
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'login.html')

def register_view(request):
    """
    Handle new user registration.

    Args:
        request: HttpRequest object containing username and passwords

    Returns:
        HttpResponse: Redirects to home page on successful registration,
                     or renders registration form with error message
    """
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'register.html', {'error': 'Las contraseñas no coinciden'})

        try:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            return redirect('home')
        except:
            return render(request, 'register.html', {'error': 'El usuario ya existe'})

    return render(request, 'register.html')

@login_required
def home_view(request):
    return render(request, 'home.html', {'username': request.user.username})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def chat_view(request):
    """
    Handle chat messages and display chat interface.

    Args:
        request: HttpRequest object containing message content in POST

    Returns:
        HttpResponse: Renders chat page with all messages or
                     redirects after posting new message
    """
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Message.objects.create(user=request.user, content=content)
        return redirect("chat")

    messages = Message.objects.all().order_by("timestamp")
    return render(request, "chat.html", {"messages": messages, "username": request.user.username})
