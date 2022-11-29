from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
""" WorkoutHistory model links to user and contains all of their workouts """
class WorkoutHistory(models.Model):
    user = models.CharField(max_length = 50, primary_key=True)  #jhowar63 - sp2:made this primary key

    def __str__(self):
        return str(self.user) + ' WorkoutHistory'


"""
Workouts are linked to user via WorkoutHistory. They are a collection 
of exercises, keyed on an ID, and contains the date of the workout
"""
class Workout(models.Model):
    date = models.DateField()
    user = models.CharField(max_length = 50)
    reffering_workouthistory = models.ForeignKey(WorkoutHistory, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user) + ': ' + str(self.date)
    

"""exercise_set
Exercises are elements of a workout. It has a preset library of names and
contains postive integer fields for weight, reps, rpe, sets of the given exercise.
This information will be obtained via forms
"""
class Exercise(models.Model):
    
    EXERCISE_NAMES = (
        ('BP', 'Bench Press'), ('DL', 'Deadlift'),
        ('OHP', 'Overhead Press'), ('FS',  'Front Squat'),
        ('PU',  'Pullup'), ('RDL', 'Romanian Deadlift'),
        ('DOP', 'Dumbbell Overhead Press'), ('HPT', 'Hip Thrust'),
        ('SQT', 'Squat'),
    )
    
    reffering_workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, choices=EXERCISE_NAMES)
    reps = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    rpe = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )



class CalorieHistory(models.Model):
    user = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.user) + ' CalorieHistory'

class Day(models.Model):
    date = models.DateField()
    user = models.CharField(max_length = 50)
    reffering_caloriehistory = models.ForeignKey(CalorieHistory, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user) + ': ' + str(self.date)

""" 
Meal categories for calorie tracker along with date of meal and
fields for the macros of the meal and quantity of them
"""
class Category(models.Model):
    options= (
        ('Breakfast','Breakfast'),
        ('lunch','Lunch'),
        ('Dinner','Dinner'),
        ('Snacks','Snacks'),
    )
    reffering_day = models.ForeignKey(Day, on_delete=models.CASCADE)
    category=models.CharField(max_length=50,choices=options)
    name = models.CharField(max_length = 50)
    carbohydrate = models.PositiveIntegerField()
    fats = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    calorie= models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

