#from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from telnetlib import LOGOUT, Telnet
from django import forms
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm

class EditProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = None
        exclude = ('groups','is_staff', 'is_active', 'user_permissions', 'is_superuser', 'password', 'last_login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'ProfilePage.html'
    success_url = reverse_lazy('home')
    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('PasswordSuccess')

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
        
        if len(username)>15:
            messages.error(request, "Username must be under 10 characters.")
            return redirect('home')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username must not contain special characters.")
            return redirect('home')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
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
            return redirect('ProfilePage')
            return render(request, "homepage.html", {'fname' : fname})
        else:
            messages.error(request, "Credentials Are Incorrect")
            return redirect('home')

    return render(request, "SignIn.html")

def SignOut(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')

def ProfilePage(request):
    user = request.user
    fname = user.first_name
    #all_workouts = Workout.objects.filter()
    return render(request, "ProfilePage.html", {'fname' : fname})

def CreateCharts(request):
    pass

def ChartHistory(request):
    pass

def MoreInfo(request):
    return render(request, "MoreInfo.html")

def CreateExercise(request):
    exercisename = request.POST.get('CExercise')
    if exercisename != '':
        messages.success(request, "Exercise made!")
    return render(request, "CreateWorkout.html", {'Exercisename' : exercisename})

# Jacob Howard working here.
def CreateWorkout(request):

    return render(request, "CreateWorkout.html")
    #return render(request, "CreateWorkout.html")

def password_success(request):
    return render(request, 'PasswordSuccess.html',{})   

