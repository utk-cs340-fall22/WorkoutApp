#from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from telnetlib import LOGOUT, Telnet
from django import forms
from django.contrib.auth.views import PasswordChangeView, PasswordChangeForm
from .models import WorkoutHistory, Workout, Exercise
from .forms import ExerciseForm

class EditProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = None
        exclude = ('groups','is_staff', 'is_active', 'user_permissions', 'is_superuser', 'password', 'last_login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'EditProfile.html'
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
    username = user.username
    workouthistory = None
    all_workouts = None
    try:
        WorkoutHistory.objects.get(user=str(username)) is not None
        workouthistory = WorkoutHistory.objects.get(user=str(username))
        all_workouts = WorkoutHistory.objects.get(user=str(username)).workout_set.all()
    except WorkoutHistory.DoesNotExist:
        raise Http404("User's WorkoutHistory does not exist")
    context = {
        'workouthistory': workouthistory,
        'all_workouts' : all_workouts,
        }
    return render(request, "ProfilePage.html", context)
    #we need to create a WorkoutHistory and pair it to user when they create their account.
    #right now this can result in error if user doesnt have wh.

def Workout_Details(request, id=None):
    specific_workout = None
    all_exercises = None
    try:    
        specific_workout = Workout.objects.get(id=id)
        all_exercises = Workout.objects.get(id=id).exercise_set.all()
    except Workout.DoesNotExist:
        raise Http404("User's Workout does not exist")
    context = {
        'specific_workout': specific_workout,
        'all_exercises': all_exercises
        }
    return render(request, "WorkoutDetails.html", context)

def CreateCharts(request):
    pass

def ChartHistory(request):
    pass

def MoreInfo(request):
    return render(request, "MoreInfo.html")

def CreateExercise(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)

    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if ExerciseForm.is_valid():
            exercise.name = form.name
            exercise.reps = form.reps
            exercise.sets = form.sets
            exercise.weight = form.weight
            exercise.rpe = form.rpe 
            # exercise.reffering_workout = CreateWorkout()??
            exercise.save()

    return render(request, "CreateWorkout.html", {'Exercisename' : exercise.name})


    """
    exercisename = request.POST.get('CExercise')
    if exercisename != '':
        messages.success(request, "Exercise made!")
    return render(request, "CreateWorkout.html", {'Exercisename' : exercisename})
    """

# Jacob Howard working here.
def CreateWorkout(request):

    return render(request, "CreateWorkout.html")
    #return render(request, "CreateWorkout.html")

def password_success(request):
    return render(request, 'PasswordSuccess.html',{})   

def EditProfile(request):
    return render(request, "EditProfile.html")
