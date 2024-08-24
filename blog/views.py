from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Profile

# Login view
def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

# Register view
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Profile

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, first_name=form.cleaned_data['first_name'], email=form.cleaned_data['email'])
            login(request, user)  # Log the user in after registration
            messages.success(request, f"Welcome {user.profile.first_name}, you have successfully registered!")
            return redirect('index')
        else:
            # If form is invalid, re-render the registration page with form errors
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

# Index view (home page)
@login_required
def index(request):
    return render(request, 'blog/index.html', {'user': request.user})

# Logout view
@login_required
def log_out(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
