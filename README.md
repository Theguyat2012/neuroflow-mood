# neuroflow-mood
Allows user registration and login for keeping track of your everyday moods.
## Setup
The FLASK_APP environment variable must be set to "mood" before being able to run this app.
For Windows, you can set FLASK_APP by using the following command:
```
$env:FLASK_APP="mood"
```
Once FLASK_APP has been set to mood, the program can start running by using the following command:
```
python -m flask run
```
## Register
You must first register an account before being able to access the '/mood' endpoint. Navigate to the '/register' endpoint by entering it into the url or clicking the "register" link at the top of the page.
<br />
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./mood/static/LogoutNav.PNG">
  <source media="(prefers-color-scheme: light)" srcset="./mood/static/LogoutNav.PNG">
  <img alt="Shows the navbar when user is not logged in" src="./mood/static/LogoutNav.PNG">
</picture>
<br />
Fill out and submit the following form to register a new account.
<br />
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./mood/static/Register.PNG">
  <source media="(prefers-color-scheme: light)" srcset="./mood/static/Register.PNG">
  <img alt="Shows the register form" src="./mood/static/Register.PNG">
</picture>
<br />

## Login
Once you have registered an account, you should navigate to the '/login' endpoint and fill out and submit the following form with your new credentials.
<br />
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./mood/static/Login.PNG">
  <source media="(prefers-color-scheme: light)" srcset="./mood/static/Login.PNG">
  <img alt="Shows the login form" src="./mood/static/Login.PNG">
</picture>

## Mood
After logging in, you now have access to the '/mood' endpoint.
<br />
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./mood/static/LoginNav.PNG">
  <source media="(prefers-color-scheme: light)" srcset="./mood/static/LoginNav.PNG">
  <img alt="Shows the mood endpoint" src="./mood/static/LoginNav.PNG">
</picture>
<br />

The user can submit a mood by clicking one of the buttons of a respective mood. A history of the user's moods will be shown below the buttons. The user's statisics is shown above the buttons.
<br />
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./mood/static/Mood.PNG">
  <source media="(prefers-color-scheme: light)" srcset="./mood/static/Mood.PNG">
  <img alt="Shows the mood endpoint" src="./mood/static/Mood.PNG">
</picture>
<br />

Users may submit any number of moods in a single day. The user's streak increment by one if the user submits at least one mood for a consecutive number of days from the current date. Once midnight is reached and the user has not submitted a mood for the current day, the streak will reset to 0.

## What would I do differently?
For a production application (disregarding the frontend aspect), there are many things I would like add. Firstly, I would take the user's timezones into account and save this data into the user models. One way I can do this is by accessing the browser's IANA timezone using javascript. My algorithm for resetting user streaks takes linear time in the worst case. It works however, I would like work on it longer to see how it can be improved if it is possible. Pagination does not currently exist for my application. Implementing it for production would be very useful for users that have a long account history.