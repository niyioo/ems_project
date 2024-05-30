from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Change 'home' to the appropriate URL name
        else:
            return render(request, 'authentication/login.html', {'error': 'Invalid username or password'})
    return render(request, 'authentication/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Change 'login' to the appropriate URL name

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Change 'login' to the appropriate URL name
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})
