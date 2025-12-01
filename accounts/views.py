from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserUpdateForm, LoginForm, ProfileUpdateForm
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


@login_required
def profileEdit(request):
    user = request.user
    user_profile = user.profile
    
    if request.method == 'POST':
        user_form = CustomUserUpdateForm(request.POST, instance=request.user)        
        user_profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and user_profile_form.is_valid():            
            user_form.save()
            user_profile_form.save()
            #obj.user = request.user
            #print("Saving profile for user:", request.user)
            #obj.save()
            return redirect('profile')
    else:    
        user_form = CustomUserUpdateForm(instance=request.user)
        user_profile_form = ProfileUpdateForm(instance=request.user.profile)
        
        context = {
            'user_form': user_form,
            'profile_form': user_profile_form,
        }
        
        return render(request, 'accounts\profile_edit.html', context)

