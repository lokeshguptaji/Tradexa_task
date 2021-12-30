from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from django.contrib.auth import authenticate,logout as deauth, login  as dj_login,get_user

# Create your views here.



def register(request):
    if request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User Is Created")
        else:
            return redirect('register')

    form = CreateUserForm()
    return render(request, 'user/register.html', {'form': form})

def login(request):
    if request.GET:
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('index')
    return render(request,'user/login.html')


def logout(request):
    if request.user.is_authenticated:
        deauth(request)

    return redirect('index')


def index(request):
    if request.method=="POST":
           user = get_user(request)
           text=request.POST.get('text','')
           post=Post(user=user,text=text)
           post.save()
    return render(request,'user/index.html')