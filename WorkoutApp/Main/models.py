from unicodedata import name
from django.db import models

# Create your models here.

# jhowar63
# Working on adding Library for exercises.
# The general idea is: 
# Every user will have a WorkoutHistory, that is a collection of Workouts.
# Every workout will be a collection of Exercises.

class WorkoutHistory(models.Model):
    pass

class Workout(models.Model):
    date = models.DateField() # Date of the workout, to keep track chronologically
    user = models.CharField()
    

class Exercise(models.Model):
    # Should link exercises to larger workout.
    # on_delete, should delete all exercises associated with workout if workout is deleted.
    EXERCISE_NAMES = (
        ('BP', 'Bench Press'),
        ('DL', 'Deadlift'),
        ('OHP', 'Overhead Press'),
    )
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, choices=EXERCISE_NAMES)
    reps = models.IntegerField()
    sets = models.IntegerField()
    weight = models.IntegerField()
    rpe = models.IntegerField() # make min = 1 and max = 10
