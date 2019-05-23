from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    return render(request, 'home/login.html')

def signup(request):
    return render(request, 'home/signup.html')

def signupHandler(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
               user = User.objects.get(username=request.POST['email'])
               return HttpResponse('Already Registered')
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['email'],password=request.POST['password1'])
                return HttpResponse('Registered')
        else:
            return HttpResponse('Password Not Matching')

def loginHandler(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return HttpResponse('1')
        else:
            return HttpResponse('0')

#def home(request):
#    if request.user.is_authenticated():
#        return render(request, 'home/home.html')
#    else:
#3        return render(request,'home/login.html')

def home(request):
    if not request.user.is_authenticated:
        return render(request,'home/login.html')
    else:
        profile = User.objects.get(username = request.user)
        return render(request, 'home/home.html')


