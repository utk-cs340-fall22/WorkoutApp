from django.contrib import admin
from .models import CalorieHistory, Workout, Exercise, WorkoutHistory

# Register your models here.
admin.site.register(WorkoutHistory)
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(CalorieHistory)
