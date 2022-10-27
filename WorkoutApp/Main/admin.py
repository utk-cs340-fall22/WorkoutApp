from django.contrib import admin
from .models import Workout, Exercise, WorkoutHistory     # jhowar63 - Adding workouts to admin info
#from .models import Exercise    # jhowar63 - Adding workout's exercises to admin info

# Register your models here.
admin.site.register(WorkoutHistory)
admin.site.register(Workout)    # jhowar63 - Adding workouts to admin view
admin.site.register(Exercise)   # jhowar63 - Adding workout's exercises to admin view
#might be too much info