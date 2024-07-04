from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request) :
    return render(request, "registration/index.html")

def signin(request) : 
    if request.method == "POST" : 
        username =  request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)
        if user is not None :
            login(request, user)
            fname = user.first_name
            return render(request, 'registration/index.html', {'fname' : fname})
        else :
            messages.error(request, "Wrong Credentials")
            return redirect('home')
    return render(request, "registration/signin.html")

def signup(request) :
    if request.method == "POST" :
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        

        # Checks on username, email, passwords etc
        if User.objects.filter(username = username) :
            messages.error(request, "Username already exists")
            return redirect('home')
        
        elif User.objects.filter(email = email) :
            messages.error(request, "Email already exists")
            return redirect('home')
        
        elif pass1 != pass2 :
            messages.error(request, "Passwords do not match")
            return redirect('home')
        
        else : 
            user = User.objects.create_user(username, email, pass1)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "Account Successfully Created")
            return redirect('signin')


    return render(request, "registration/signup.html")

def signout(request) : 
    logout(request)
    messages.success(request, "Logged you out of your account")
    return redirect('home')

