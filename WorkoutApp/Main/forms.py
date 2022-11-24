from django import forms
from .models import Exercise, Category

""" This is the form fields for making an exercise from user input """
class ExerciseForm(forms.Form):
    name = forms.CharField(label="Exercise Name", widget=forms.Select(choices=Exercise.EXERCISE_NAMES))
    sets = forms.IntegerField(min_value=0, label="Number of Sets")
    reps = forms.IntegerField(min_value=0, label="Number of Reps")
    weight = forms.IntegerField(min_value=0, label="Weight in lbs")
    rpe = forms.IntegerField(min_value=0, max_value=10, label="RPE")


""" Form fields for user to create workout (just date) """
class WorkoutForm(forms.Form):
    date = forms.DateField(label='Enter Date of Workout')

class DayForm(forms.Form):
    date = forms.DateField(label='Enter the Date of Meals Eaten')



""" Form fields for user to log meal information and calories/macros """
class CalorieForm(forms.Form):
    category = forms.CharField(label="Meal", widget=forms.Select(choices=Category.options))
    name = forms.CharField(label="Food's Name")
    carbohydrate = forms.DecimalField(min_value=0, label="Amount of Carbs (g)")
    fats = forms.DecimalField(min_value=0, label="Amount of Fat (g)")
    protein = forms.DecimalField(min_value=0, label="Amount of Protein (g)")
    calorie= forms.DecimalField(min_value=0, label="Amount of Calories (g)")
    quantity = forms.DecimalField(min_value=0, label="Amount Consumed (g)")
