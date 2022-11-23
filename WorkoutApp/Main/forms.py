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



""" Form fields for user to log meal information and calories/macros """
class CalorieForm(forms.Form):
    date = forms.DateField(label='Enter Date of Meals')
    category = forms.CharField(label="Exercise Name", widget=forms.Select(choices=Category.options))
    carbohydrate = forms.IntegerField(min_value=0, label="Amount of Carbs")
    fats = forms.IntegerField(min_value=0, label="Amount of Fat")
    protein = forms.IntegerField(min_value=0, label="Amount of Protein")
    calorie= forms.IntegerField(min_value=0, label="Amount of Calories")
    quantity = forms.IntegerField(min_value=0, label="Amount Consumed")
