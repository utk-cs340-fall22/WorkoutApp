"""WorkoutApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import ProfilePage, UserEditView, PasswordsChangeView, Workout_Details
from . import views
from django.contrib.auth import views as auth_views


#Creating all the urls for the website
urlpatterns = [
    path('', views.home, name="home"),
    path('CreateAccount', views.CreateAccount, name='CreateAccount'),
    path('SignIn', views.SignIn, name='SignIn'),
    path('SignOut', views.SignOut, name='SignOut'),
    path('ProfilePage', views.ProfilePage, name='ProfilePage'),   #changing UserEditView.as_view() to views.ProfilePage
    path('CreateCharts', views.CreateCharts, name='CreateCharts'),
    path('ChartHistory', views.ChartHistory, name='ChartHistory'),
    path('MoreInfo', views.MoreInfo, name='MoreInfo'),
    path('CreateWorkout', views.CreateWorkout, name='CreateWorkout'),
    path('CreateWorkout2', views.CreateWorkout2, name='CreateWorkout2'),
    path('password/', PasswordsChangeView.as_view(template_name='ChangePassword.html')),
    path('password_success', views.password_success, name='PasswordSuccess'),
    path('ProfilePage/<int:id>/Workouts', views.Workout_Details),
    path('ProfilePage/<int:id>/add-exercise', views.CreateExercise),
    path('EditProfile', UserEditView.as_view(), name='EditProfile'),
    path('delete-item/<int:id>', views.deleteItem, name="delete-item"),
    path('delete-workout/<int:id>', views.deleteWorkout, name="delete-workout"),
    path('ProfilePage/<int:id>/ConfirmDeletion', views.confirmWorkoutDelete, name="ConfirmDeletion"),
    path('ProfilePage/<int:id>/Meals', views.calorie_tracker, name='CalorieTracker.html'),
    path('ProfilePage/TestCharts', views.TestCharts, name='TestCharts'),    #jhowar63 - for testing graph stuff.
    path('CreateTracker', views.CreateTracker, name='CreateTracker'),
    path('ProfilePage/<int:id>/add-meal', views.CreateMeal),
    path('delete-meal/<int:id>', views.deleteMeal, name="delete-meal"),
    path('ProfilePage/<int:id>/ConfirmMealDeletion', views.confirmMealDelete, name="ConfirmMealDeletion"),
    path('delete-day/<int:id>', views.deleteDay, name="delete-day"),
    path('index', views.index, name='index'),
]
