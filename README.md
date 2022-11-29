# WorkoutApp
## Group Members
* Andrew Hines - [mdew-abc](https://github.com/mdew-abc)
* Jacob Howard - [jhowar63](https://github.com/jhowar63)
* Alex Shirran - [Ashirran](https://github.com/Ashirran)
* Justin Bowers - [NutsRobin](https://github.com/NutsRobin)
* Michael Gibson - [Mgibso46](https://github.com/Mgibso46)


# About WorkoutApp

 WorkoutApp is a web application built with Django that allows users to log and analyze their workouts and meals

#
# How to run

1. Be sure to have [Python3](https://www.python.org/downloads/) installed on your machine.

2. Clone the repo by runnning the command `git clone https://github.com/utk-cs340-fall22/WorkoutApp.git` in your terminal/command prompt.

3. Create a [python virtual enviorment](https://docs.python.org/3/tutorial/venv.html) and activate it.

4. Run the following commands
   ```
   pip install -r requirements.txt
   cd WorkoutApp
   python3 manage.py runserver
   ```

5. Now go to http://127.0.0.1:8000/ which should display the homepage. (add a screenshot here of final homepage)

#
# How to use

To use are product, you must create a free account. To create a free WorkoutApp account, you must first make sure you are on the homepage at http://127.0.0.1:8000. Then, you must click the create account button, and enter your credentials. Once you are finished, click "Sign up!". This will send you back to the homepage. Once this is complete, or if you had an account from before, then click the "Sign In" button at the top left to sign in. After you put in your username and password, pressing the sign in button below will take you to your accounts home page.

### Homepage

Homepage simply is a page we use as a default for when there is no where else to go. Not much is done here.

### Create new workout

This is to create a new workout using a date. Either type the date as "mm/dd/yyy" or "Month day, year".

### Create New Meal

Same as Create New Workout, but for meals.

### Profile Page

Profile Page has many options to choose from. You are able to change your account information using the Edit Profile button. You can also use the chart under the Edit Profile button to see how you are doing with your workouts. Below that, there is a history of workouts and meals listed by date, which you can click individually to add exercises/meal into them. When you add an Exercise, you must input the exercise name, set amount, rep amount, weight, and RPE. Once added, you can add another exercise to the same workout, or go back to the profile page. Doing this will adjust the plot to show you more information on how you are doing. You can also delete exercises and workouts, however workouts require extra confirmation.

### Sign out

Signs you out of your account. 

### More info

Gives information on how to be more effective at working out and eating healthy.
