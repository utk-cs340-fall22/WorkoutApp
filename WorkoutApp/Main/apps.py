from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Main'

# jhowar63
# A tutorial I watched did this when they added models so I am.
# Not sure if it is necessary or correct.
# class WorkoutAppConfig(AppConfig):
   # name = 'WorkoutApp'