from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from telnetlib import LOGOUT


# Create your views here.
def home(request):
    return render(request, "homepage.html")

def CreateAccount(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists!")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already exists!")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters.")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")

        if not username.isalnum():
            messages.error(request, "Username must not contain special characters.")
            return redirect('home')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save() 

        messages.success(request, "Your Account has been successfully created.")
        return redirect('home')
    return render(request, "CreateAccount.html")

def SignIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "Login/index.html", {'fname' : fname})
        else:
            messages.error(request, "Credentials Are Incorrect")
            return redirect('home')

    return render(request, "SignIn.html")

def SignOut(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')

def CreateCharts(request):
    pass

def ChartHistory(request):
    pass

def MoreInfo(request):
    pass
