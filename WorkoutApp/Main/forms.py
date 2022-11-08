from django import forms
from .models import Exercise, Category

class ExerciseForm(forms.Form):
    name = forms.CharField(label="Exercise Name", widget=forms.Select(choices=Exercise.EXERCISE_NAMES))
    sets = forms.IntegerField(min_value=0, label="Number of Sets")
    reps = forms.IntegerField(min_value=0, label="Number of Reps")
    weight = forms.IntegerField(min_value=0, label="Weight in lbs")
    rpe = forms.IntegerField(min_value=0, max_value=10, label="RPE")

class WorkoutForm(forms.Form):
    date = forms.DateField(label='Enter Date of Workout')

class ExerciseForm(forms.Form):
    name = forms.CharField(label="Exercise Name", widget=forms.Select(choices=Exercise.EXERCISE_NAMES))
    sets = forms.IntegerField(min_value=0, label="Number of Sets")
    reps = forms.IntegerField(min_value=0, label="Number of Reps")
    weight = forms.IntegerField(min_value=0, label="Weight in lbs")
    rpe = forms.IntegerField(min_value=0, max_value=10, label="RPE")

class CalorieForm(forms.Form):
    date = forms.DateField(label='Enter Date of Meals')
    category = forms.CharField(label="Exercise Name", widget=forms.Select(choices=Category.options))
    carbohydrate = forms.IntegerField(min_value=0, label="Amount of Carbs")
    fats = forms.IntegerField(min_value=0, label="Amount of Fat")
    protein = forms.IntegerField(min_value=0, label="Amount of Protein")
    calorie= forms.IntegerField(min_value=0, label="Amount of Calories")
    quantity = forms.IntegerField(min_value=0, label="Amount Consumed")
