# Sprint 4

(include your name, github id, and group name here)
Andrew Hines
github id-mdewabc,mdew-abc(I had to do work on a different computer that happened to be signed into my other github, both accounts are mine)
Workout App

### Files you worked on
* WorkoutApp/WorkoutApp/Templates/CalorieTracker.html
* WorkoutApp/WorkoutApp/Templates/ConfirmMealDelete.html
* WorkoutApp/WorkoutApp/Templates/ConfirmWorkoutDelete.html
* WorkoutApp/WorkoutApp/Templates/CreateExercise.html
* WorkoutApp/WorkoutApp/Templates/CreateMeal.html
* WorkoutApp/WorkoutApp/Templates/EditProfile.html
* WorkoutApp/WorkoutApp/Templates/MoreInfo.html
* WorkoutApp/WorkoutApp/Templates/ProfilePage.html
* WorkoutApp/WorkoutApp/Templates/WorkoutDetails.html
* WorkoutApp/WorkoutApp/Templates/homepage.html
* WorkoutApp/WorkoutApp/Main/models.py
* WorkoutApp/WorkoutApp/Main/urls.py
* WorkoutApp/WorkoutApp/Main/views.py
* WorkoutApp/WorkoutApp/static/images/gymicons.png
* WorkoutApp/WorkoutApp/static/images/workouticon.png



### What you accomplished
(Give a description of the features you added or tasks you accomplished. Provide some detail here. This section will be a little longer than the bulleted lists above)
* Changed home page image carousel to fit in the new Google API template.
I changed the width of the scrolling images to a fixed width. used gimp to ensure the images all had the same size so they wouldn't move page content 
when switching between images. Also set the images to scroll on a 4.5 second delay
* Logo
I found a creative commons licensed open source image that is avaliable for public use. I edited it in GIMP to change some the color,
size, and slightly alter the pixel art so it would fit our site. I then added that logo in the top left of each page.
* Added workout and meals interface to sidebar on homepage and more info page
* Implemented the new API template on delete workout page, and delete meal page.
* Added cancellation buttons to delete workout page and delete meal page, so that user must confirm if they would like to delete the data,
and if not they will be returned to their profile.
* Removed old broken buttons and links that are no longer used from all pages.
I removed old links to Test Graph and other pages that we no longer are using, also removed the "Create Account", "Forgot Password", and "Sign In" buttons from the navigation
bar on all pages if the user is already signed into an account