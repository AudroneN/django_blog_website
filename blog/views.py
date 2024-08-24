from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegistrationForm, BlogPostForm
from .models import Profile, BlogPost

# home page
@login_required
def index(request):
    blog_posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/index.html', {'user': request.user, 'blog_posts': blog_posts})

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



# Logout view
@login_required
def log_out(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')





@login_required
def create_blog_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            messages.success(request, "Blog post created successfully!")
            return redirect('index')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html', {'form': form})

@login_required
def edit_blog_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk, author=request.user)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog post updated successfully!")
            return redirect('index')
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'blog/edit_blog_post.html', {'form': form})

@login_required
def delete_blog_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk, author=request.user)
    if request.method == "POST":
        blog_post.delete()
        messages.success(request, "Blog post deleted successfully!")
        return redirect('index')
    return render(request, 'blog/delete_blog_post.html', {'blog_post': blog_post})
