# Sprint 2

Name: Jacob Howard

Github ID: jhowar63

Group Name: WorkoutApp

### What you planned to do
- Associate WorkoutHistory and all its sub-models with their user. https://github.com/utk-cs340-fall22/WorkoutApp/issues/23
- Display a list of all the Workouts that Compose a User's WorkoutHistory on their Profile Page. https://github.com/utk-cs340-fall22/WorkoutApp/issues/24
- Make it so that the user's list of workouts on their Profile Page are links that bring you to a summary of that workout. https://github.com/utk-cs340-fall22/WorkoutApp/issues/25


### What you did not do
- Ideally when you click on a Workout on a User's Profile Page it would open up a drop down that displays the workout summary with the option to take them to the dedicated workout summary page.
  Rather than just automatically linking it to the workout summary page.

### What problems you encountered
- This sprint I primarily worked with the projects backend. One of the things I wanted to do was display information regarding a User's Workouts and Exercises.
  This proved very difficult to test and implement because when I was working we did not have a way for users input to be stored in the database.
  So I had to spend a lot of time figuring out how to manually save data to the database, that I could then use to test what I was implementing.
- When we make changes that effect the database they only exist locally, so I had a lot of difficulty creating a common primary DB that everyone could use for  testing.
- None of these issues and changes are easily visable because they effect WorkoutApp/dbsqlite3 a binary file.

### Issues you worked on
- Associate WorkoutHistory and all its sub-models with their user. https://github.com/utk-cs340-fall22/WorkoutApp/issues/23
- Display Workouts that Compose a User's WorkoutHistory on their Profile Page. https://github.com/utk-cs340-fall22/WorkoutApp/issues/24
- Workouts in User's WorkoutHistory should be links to the workout's summary. https://github.com/utk-cs340-fall22/WorkoutApp/issues/25

### Files you worked on
- WorkoutApp/Main/admin.py
- WorkoutApp/Main/models.py
- WorkoutApp/Main/urls.py
- WorkoutApp/Main/views.py
- WorkoutApp/Templates/homepage.html
- WorkoutApp/Templates/WorkoutDetails.html
- WorkoutApp/dbsqlite3

### What you accomplished

This sprint I worked mainly on the WorkoutApp backend. 
I implemented a many to one relationship for Exercises to Workout and also for Workouts to WorkoutHistory.
I made it so that when a User views their profile page it displays a list of all their past workouts by date.
This list works displays Workouts as dynamic urls that when clicked will bring the User to a html page I made called WorkoutDetails, which displays a summary of the selected workout.
I also created a base database that contains a user named primary that all current and future testing is being done on.
I also cleaned up some bugs when a user that has not created a profile tries to view any of the pages besides the home page and sign in page.
Throughout this sprint I have grown so much more familiar and confident with django, especially working with its database.
