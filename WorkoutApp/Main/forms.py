from django import forms

class ExerciseForm(forms.Form):
    name = forms.CharField(help_text="Exercise name")
    sets = forms.IntegerField(min_value=0, help_text="Number of sets")
    reps = forms.IntegerField(min_value=0, help_text="Number of reps")
    weight = forms.IntegerField(min_value=0, help_text="Weight in lbs")
    rpe = forms.IntegerField(min_value=0, max_value=10, help_text="RPE")

class WorkoutForm(forms.Form):
    date = forms.DateField(help_text='Enter date of workout')
