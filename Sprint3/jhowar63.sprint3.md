# Sprint 2

Name: Jacob Howard

Github ID: jhowar63

Group Name: WorkoutApp

### What you planned to do
- This sprint I planned on working primarily with charts to display our information graphically.
- Originally I planned to do so using matplotlib.
- I also wanted to spend some time working on how we were going to display information about and on the CalorieTracker pages.
- Spend time testing the website, recording bugs that need to be fixed.


### What you did not do
- I was not able to connect our database to the graphs.
- I was also not able to get matplotlib to work, we have since decided as a group to switch to plotly for graphing.

### What problems you encountered
- matplotlib was our initial thought for how we were going to display our database information graphically. 
  It did not work or even have all of the functionality we were hoping for, so we decided fairly last minute to switch to plotly.

### Issues you worked on
- Create a graph that reflects a users WorkoutHistory
- Create a graph that displays information regarding a specific workout.
- Work on the displays and integration of the CalorieTracker.

### Files you worked on
- WorkoutApp/Main/urls.py
- WorkoutApp/Main/views.py
- WorkoutApp/Templates/CalorieDetails.html
- WorkoutApp/Templates/CalorieTracker.html
- WorkoutApp/Templates/ProfilePage.html
- WorkoutApp/Templates/TestCharts.html


### What you accomplished
This sprint I worked mainly on creating graphs that can display information regarding a user’s WorkoutHistory, their individual workouts, and their calorie/meal history. 
I created three interactive graphs, one for each item in the previous list. 
This is still being stored in a test html page because it is not yet fully ready to move to our WorkoutDetails page (its a lot easier to bug test this way). 
I also created pages that display a user's calorie and meal history, this is yet to allow entries to be stored in our database, but it serves as our base. 
Finally I spent time navigating the site testing and recording bugs I encountered.
