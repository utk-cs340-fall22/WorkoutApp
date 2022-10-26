# Sprint 1

Name: Alex Shirran

Github ID: Ashirran

Group Name: WorkoutApp

### What you planned to do
- Learn how to add images and hyperlinks to Django : https://github.com/utk-cs340-fall22/WorkoutApp/issues/30
- Construct the more info page : https://github.com/utk-cs340-fall22/WorkoutApp/issues/28
- Create the password edit page and create a button to access it in the profile page : https://github.com/utk-cs340-fall22/WorkoutApp/issues/27
- Create the ability to edit your profile : https://github.com/utk-cs340-fall22/WorkoutApp/issues/26

### What you did not do
- Create as much in depth details on the more info page

### What problems you encountered
- I had a lot of issues adding pictures to html documents in Django at first
- Trying to get rid of certain fields in the profile edit page (At first users could make themselves admins, etc)
- Making sure the more info page looked good (picture size, html links working properly)

### Issues you worked on
- Create the ability to edit your profile : https://github.com/utk-cs340-fall22/WorkoutApp/issues/26
- Create the password edit page and create a button to access it in the profile page : https://github.com/utk-cs340-fall22/WorkoutApp/issues/27
- Construct the more info page : https://github.com/utk-cs340-fall22/WorkoutApp/issues/28
- Learn how to add images and hyperlinks to Django : https://github.com/utk-cs340-fall22/WorkoutApp/issues/30

### Files you worked on
- WorkoutApp/Main/urls.py
- WorkoutApp/Main/views.py
- WorkoutApp/Templates/ChangePassword.html
- WorkoutApp/Templates/PasswordSuccess.html
- WorkoutApp/Templates/ProfilePage.html
- WorkoutApp/Templates/homepage.html
- WorkoutApp/Templates/CreateWorkout.html
- WorkoutApp/Templates/MoreInfo.html
- WorkoutApp/WorkoutApp/settings.py
- WorkoutApp/Templates/EditProfile.html

### What you accomplished
First I researched how to edit a users profile on django. Then once I got all of the account fields showing up on the website, I had a lot of trouble trying to find a way to get rid of fields such as: 'groups', 'is_staff', 'is_active', 'user_permissions', 'is_superuser', 'last login'. Then I noticed that the password edit section brings the user to the Django Admin section so I needed to change it to where they could change their password using a form on our website itself rather than the Django admin page. After that I learned how to add images to Django, I tried using a way that required the use of a media folder and went through all the steps only to find out the steps I was looking at was for an older version of Django. So I found a way to add images to a website correctly. Then after that, I was required to change the user profile page edit section and add it to a new html on its own.