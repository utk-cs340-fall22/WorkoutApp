from django.contrib import admin
from .models import Workout, Exercise, WorkoutHistory

# Register your models here.
admin.site.register(WorkoutHistory)
admin.site.register(Workout)
admin.site.register(Exercise)