from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# jhowar63
# Working on adding Library for exercises.
# The general idea is: 
# Every user will have a WorkoutHistory, that is a collection of Workouts.
# Every workout will be a collection of Exercises.

class WorkoutHistory(models.Model):
    user = models.CharField(max_length = 50, primary_key=True)  #jhowar63 - sp2:made this primary key

    def __str__(self):
        return str(self.user) + ' WorkoutHistory'

class Workout(models.Model):
    date = models.DateField() # jhowar63 - sp1:Date of the workout, to keep track chronologically. sp2:made this pk
    user = models.CharField(max_length = 50)
    reffering_workouthistory = models.ForeignKey(WorkoutHistory, on_delete=models.CASCADE)
    
#jhowar63 - changing how workouts are named in database.
    def __str__(self):
        return str(self.user) + ': ' + str(self.date)
    

class Exercise(models.Model):
    # Should link exercises to larger workout.
    # on_delete, should delete all exercises associated with workout if workout is deleted.
    EXERCISE_NAMES = (
        ('BP', 'Bench Press'),
        ('DL', 'Deadlift'),
        ('OHP', 'Overhead Press'),
    )
    reffering_workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, choices=EXERCISE_NAMES)
    reps = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    rpe = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
