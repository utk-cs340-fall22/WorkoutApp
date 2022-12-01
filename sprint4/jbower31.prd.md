# Product Requirements Document: PyCoach
Name: Justin Bowers

## Background
Tracking and logging workout and caloric information is an extremely important part of reaching one's fitness goals. Whether it be to lose fat, gain muscle, or training for some athletic event. This is how to keep track of progress and gague the intensity of training sessions to come. Many people, myself included, just use some basic form of notes such as on smartphones or even just good ol pen and paper. Some that would like to get more invloved use spreadsheets. However, spreadsheet are not exactly intuitive or user friendly for a typical gym goer. This leaves space for a user friendly way for anyone to easily track their progress and for effective computer analysis to be done without a steep learning curve. The other benefit is that unlike a spreadsheet, a web app can automatically do the analysis and even create suggestions for the user that are adjusted to their set goals.

## Project Overview
PyCoach is an online platform that allows users to easily and effectively log, track, and analyze their fitness journey. With simple UI anyone can achieve a much deeper look into their performance and use this to make more informed decisions regarding their training and nutrition. Or should a user prefer guided training, PyCoach can make suggestions based on the user's goals by using real data and evidence-based algorithms. 

PyCoach also allows user's to track their nutrtion details. Nutrition is one of the most important aspects of achieving fitness goals, so PyCoach can use these details to help measure progress and update the user weekly on any changes that could help them reach their goals. With science based algorithms, real-world data, and the user's hardwork, it should help anyone achieve their fitness goals.

## Features
Give at least 8 user stories to describe required features. These can come from the issues assigned to you during the 4 sprints, or you 
can create new items. Give a title or feature name for each story. Example: 
1. **User Logs A Workout.** As a user, I want to log my most recent workout for easy viewing
2. **Create Account.** As a new user, I want to register by creating a username and password and adding some personal data so that the system may remember me and keep track of my data
3. **User Logs Meal Information** As a user, I want to track my calories so that I may better monitor my nutrtional goals
4. **User Logs Bodyweight** As a user, I want to log my weight daily so that I may easily see my progress toward my bodyweight goals
5. **Visualize Workout Data** Users will be able to see their workout data and trends in a line chart to visualize their progress
6. **Visualize Calorie Intake** Users will be able to see their daily intake in realtion to their goals as a bar chart and their total calories by percentage of macronutrients as a pie chart to better understand their nutrition
7. **Make Training Suggestion** As a new gym goer, I want to PyCoach to make automatic trianing suggestions based on my goals using science based algorithms 
8. **Make Nutrition Suggestion** As a new gym goer, I want to PyCoach to make automatic dietarybsuggestions based on my goals using science based algorithms to help me reach my bodyweight goals

## Technologies to be used
- Python
    - Django: for simple creation of a webapp with Python and HTML
    - Plotly: for data visualization
    - Pandas: for data analysis and manipulation
    - Scikit-learn: works with pandas and plotly for machine learning
    - Numpy: utilized by scikit-learn
- HTML
- CSS