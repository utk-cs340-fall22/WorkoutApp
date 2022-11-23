#from asyncio.windows_events import NULL
from datetime import datetime
import imp
from turtle import width
from django.http import HttpResponse, Http404
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
from matplotlib.style import context
import plotly
from pyparsing import ungroup
from .models import WorkoutHistory, Workout, Exercise, Category
from .forms import ExerciseForm, WorkoutForm, CalorieForm
from django.http import HttpResponseRedirect
import matplotlib as plt
import numpy as py
from io import StringIO
import plotly.express as px
import pandas as pd

"""
These three functions are used for user's to change some of their profile
information such ass password, username, name, etc...
"""
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



""" returns the homepage """
def home(request):
    return render(request, "homepage.html")



"""
This brings user to CreateAccount.html and opens a form to input account
information. It also creates an instance of a Workouthistory to track their
workouts
"""
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
        workouthistory = WorkoutHistory()
        workouthistory.user = username
        workouthistory.save()
        
        messages.success(request, "Your Account has been successfully created.")
        return redirect('home')
    return render(request, "CreateAccount.html")



""" 
This goes to SignIn.html and presents user with a login screen
It sends an error message with the use of invalid credentials
"""
def SignIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('home')
        else:
            messages.error(request, "Credentials Are Incorrect")
            return redirect('home')

    return render(request, "SignIn.html")



""" Logs user out of website and returns them to the homepage"""
def SignOut(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')



""" 
ProfilePage contains user information, and links to several important
features such as EditProfile, WorkoutHistory, Workout Graphs, and
calorie history
"""
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



""" List the details of the specified workout """
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
        'all_exercises': all_exercises,
    }
    return render(request, "WorkoutDetails.html", context)



""" WORK IN PROGRESS """
def CreateCharts(request):

    user = request.user
    username = user.username
    all_workouts = None
    try:
        WorkoutHistory.objects.get(user=str(username)) is not None
        all_workouts = WorkoutHistory.objects.get(user=str(username)).workout_set.all()
    except WorkoutHistory.DoesNotExist:
        raise Http404("User's WorkoutHistory does not exist")

    exercise_names = []
    exercise_weight = []
    dates = []
    
    for workout in all_workouts:
        exercises = Workout.objects.get(id=workout.id).exercise_set.all()
        for exercise in exercises:
            dates.append(workout.date)
            exercise_weight.append(exercise.weight)
            exercise_names.append(exercise.name)
    

    df = pd.DataFrame({
        "Exercise": exercise_names,
        "Weight" : exercise_weight,
        "Dates": dates
    })

    fig = px.line(df, x='Dates', y='Weight', color='Exercise', markers=True,
                  width=1300, height=600)
    div = plotly.offline.plot(fig, auto_open=False, output_type="div",)

    context = {
        'graph' : div
    }
    return render(request, "CreateCharts.html", context)



""" WORK IN PROGRESS """
def ChartHistory(request):
    pass



""" Navigates to the MoreInfo page """
def MoreInfo(request):
    return render(request, "MoreInfo.html")



""" 
This adds an exercise to the given workout. User gives workout
information via a form which then adds the exercise to the data table
"""
def CreateExercise(request, id):

    if request.method == 'POST':
        form = ExerciseForm(request.POST)

        if form.is_valid():
            exercise = Exercise()
            workout = Workout.objects.get(id=id)
            exercise.name = form.cleaned_data['name']
            exercise.reps = form.cleaned_data['reps']
            exercise.sets = form.cleaned_data['sets']
            exercise.weight = form.cleaned_data['weight']
            exercise.rpe = form.cleaned_data['rpe']
            exercise.reffering_workout = workout
            exercise.save()

            return redirect(request.path_info)
        
    else:
        form = ExerciseForm()
        
    return render(request,
                "Createexercise.html",
                {'form' : form})   
    

"""
Takes user to a page where they simply input the date of workout.
This creates a new workout instance which they can fill with exercises
using CreateExercise. Workouts are keyed on auto-generated ID
"""
def CreateWorkout(request):

    if request.method == 'POST':
        form = WorkoutForm(request.POST)

        # create a workout instance and fill with form data
        if form.is_valid():
            workout = Workout()
            user = request.user
            username = user.username
            workout.date = form.cleaned_data['date']
            workout.user = username
            workout.reffering_workouthistory = WorkoutHistory.objects.get(user=str(username))
            workout.save()

            return redirect('ProfilePage')

    else:
        form = WorkoutForm()

    return render(request,
                  "CreateWorkout.html",
                  {'form' : form})


""" Page to test charts """
def TestCharts(request):
    return render(request, "TestCharts.html")

""" ???? """
def CreateWorkout2(request):
    Workoutname = request.POST.get('CWorkout')
    Workoutinfo = get_object_or_404(Workout, pk=1)
    user = request.user
    
    Workoutinfo.date = Workoutname
    Workoutinfo.user = user

    if Workoutinfo.date != '':
        messages.success(request, "Workout made!")
    return render(request, "CreateExercise.html", {'WorkoutName' :Workoutinfo.date})



""" Navigates to page after successful password change """
def password_success(request):
    return render(request, 'PasswordSuccess.html',{})   


""" Returns EditProfile Page """
def EditProfile(request):
    return render(request, "EditProfile.html")


""" Deletes a Exercise from its corresponding workout """
def deleteItem(request, id):
    item = Exercise.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


""" Confirmation page to delete a Workout """
def confirmWorkoutDelete(request,id=None):
    specific_workout = None
    all_exercises = None

    try:    
        specific_workout = Workout.objects.get(id=id)
        all_exercises = Workout.objects.get(id=id).exercise_set.all()
    except Workout.DoesNotExist:
        raise Http404("User's Workout does not exist")

    context = {
        'specific_workout': specific_workout,
        'all_exercises': all_exercises,
    }
    return render(request, "ConfirmWorkoutDelete.html", context)


""" Deletes specified workout and all exercises within it """
def deleteWorkout(request,id):
    item = Workout.objects.get(id=id)
    item.delete()
    return redirect('ProfilePage')



""" Details of users calorie logs """
def Calorie_Details(request, id=None):
    all_days = None

    try:    
        all_days = Category.objects.get(id=id)
    except Category.DoesNotExist:
        raise Http404("User's Workout does not exist")

    context = {
        'all_days': all_days
    }
    return render(request, "CalorieDetails.html", context)


""" returns calorie tracking page """   
def calorie_tracker(request):
    return render(request, "CalorieTracker.html")