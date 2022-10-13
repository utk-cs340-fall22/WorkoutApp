# Sprint 1 

Andrew Hines
Github: mdew-abc
Group Name: WorkoutApp


### What you planned to do
* Familiarize myself with Django and finish the short tutorial.[#9](https://github.com/utk-cs340-fall22/WorkoutApp/issues/9)
* Create a CSS Stylesheet that serves as a basic layout so we can format each page consistently.[#6](https://github.com/utk-cs340-fall22/WorkoutApp/issues/6)
* Create a static folder in Django and modify settings.py so that our pages could use CSS stylesheets and images. [#15](https://github.com/utk-cs340-fall22/WorkoutApp/issues/15)



### What you did not do
* I had planned to spend more time studying the specifics of Django.
* I also didn't successfully implement the statics folder until in class Thursday morning while waiting to demo it.
* I had already made the stylesheet but I hadn't been able to make it work with Django until that morning. 

### What problems you encountered
* I spent a lot of time struggling with implementing the CSS stylesheet. I was viewing the html in my browser while coding and didn't realize until after that normal stylesheet links don't work when the server is being run with Django.
* I had to make a statics folder and change the settings.py folder so Django would recognize the path.
* As I tried to learn how to implement the statics folder I kept finding different syntax and commands to set it up from the past ten years, it was difficult to find the correct solution as Django has changed this many times.

### Issues you worked on
* Familiarize myself with Django and finish the short tutorial.[#9](https://github.com/utk-cs340-fall22/WorkoutApp/issues/9)
* Create a CSS Stylesheet that serves as a basic layout so we can format each page consistently.[#6](https://github.com/utk-cs340-fall22/WorkoutApp/issues/6)
* Create a static folder in Django and modify settings.py so that our pages could use CSS stylesheets and images. [#15](https://github.com/utk-cs340-fall22/WorkoutApp/issues/15)

### Files you worked on
* ahines9-sprint.md
* WorkoutApp/Templates/CreateAccount.html
* WorkoutApp/Templates/CreateWorkout.html
* WorkoutApp/Templates/ProfilePage.html
* WorkoutApp/Templates/SignIn.html
* WorkoutApp/Templates/homepage.html
* WorkoutApp/Main/views.py
* WorkoutApp/WorkoutApp/settings.py
* WorkoutApp/static/styles.css

### What you accomplished
* I finished the Django tutorial to install the software
* I finished a tutorial on the Django website that taught me how to create a simple Polls webpage.
* I added formatting and lorem ipsum placeholder text to homepage.html and ProfilePage.html 
* I created a CSS stylesheet that will allow us to change how our website looks across all pages by changing one file.
* I created and implemented a statics folder that will allow us to use CSS stylesheets as well as images in our pages.
* I created a floating Navigation Menu that will follow the user as they scroll, allowing them to navigate to any page at any time.
* I set the signin/signout button on the navigation bar to display "Signout" if the user is signed in, and "Signin" if the user isn't currently signed into an active account.