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
    path('CreateExercise', views.CreateExercise, name='CreateExerceise'),
    path('password/', PasswordsChangeView.as_view(template_name='ChangePassword.html')),
    path('password_success', views.password_success, name='PasswordSuccess'),
    path('ProfilePage/<int:id>/', views.Workout_Details),
    path('EditProfile', UserEditView.as_view(), name='EditProfile'),
]
