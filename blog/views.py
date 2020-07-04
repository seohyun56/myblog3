from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBlog
from .models import Blog
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import UserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .forms import LoginForm
from django.contrib.auth import logout


# Create your views here.
def index(request):
    return render(request, 'index.html')

def music(request):
    return render(request, 'music.html')

def photo(request):
    return render(request, 'photo.html')

def visitors(request):
    blogs = Blog.objects.all()
    return render(request, 'profile.html', {'blogs':blogs})

def sns(request):
    return render(request, 'sns.html')

def timetable(request):
    return render(request, 'timetable.html')

@login_required
def createBlog(request):

    if request.method == 'POST':
        form = CreateBlog(request.POST)

        if form.is_valid():
            form.save()
            return redirect('visitors')
        else:
            return redirect('index')
    else:
        form = CreateBlog()
        return render(request, 'createBlog.html', {'form':form})


def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Login failed. Try again.')
    else:
        form = LoginForm()
        return render(request, 'user_login.html')

def signout(request):
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
    else:
        form = UserForm()
        return render(request, 'user_new.html')