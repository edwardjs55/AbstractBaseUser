from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


# Login View
def login_view(request):
    if request.method == 'POST':
        if not LoginForm(request.POST).is_valid(): # my addition
            return
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            print("  "+ username + " - login rejected")
            messages.error(request, 'Invalid credentials')
    form = LoginForm()
    return render(request, 'accounts\login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'accounts\profile.html')

