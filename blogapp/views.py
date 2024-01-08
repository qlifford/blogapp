from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import *
from .forms import *

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    form = BlogForm
    pic = RegUser.objects.all()
    context = {'blogs': blogs, 'form': form, 'pic': pic}
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'blogs/index.html', context)


def detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {'blog': blog}
    return render(request, 'blogs/detail.html', context)

def delete_post(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    return redirect('/')

def like(request, pk):
    blog = Blog.objects.get(pk=pk)
    return redirect('/', args[pk] )

def reg(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = UserForm
        if request.method == 'POST':
            form = UserForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                user = form.save()
                if user is not None:
                    login(request, user)
                    return redirect('/')
        context = {'form': form}
        return render(request, 'registration/register.html', context)

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        return render(request, 'registration/login.html')

def sign_out(request):
    logout(request)
    return redirect('/')

