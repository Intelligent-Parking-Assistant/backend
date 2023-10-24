# IPA backend
# Project setup
Below are some of the steps to take for full setup:
1. Run the following command ```pip install -r requirements.txt```
2. ```cd backend```
3. Run the migrations ```python manage.py migrate```
4. Start the project, ```python manage.py runserver```
You should then be all set
# Navigating the site
1. Registration of users: ```localhost:8000/accounts/users/```
2. Creating a user's profile: ```localhost:8000/accounts/profile/```
3. Directions: ```localhost:8000/directions/```
4. Search: ```localhost:8000/search/```
5. Visits: ```localhost:8000/visits/<id>/```

# Postgress Setup
1. Download pgAdmin: ```https://www.postgresql.org/download/```
2. Follow the wizard setup and take note of the password and username
3. In the root directory of the project create an .env file
4. Populate it with the username and password
