Continue from 22_travel_proj_basic_setup

1) Run the command to create new app named "tour_app"
\travel_proj\travel_proj>python manage.py startapp tour_app

2) Create the following folders under app "tour_app"

- templates
  |-tour_app
- static
  |-tour_app
    |- css
    |- img
    |- js

3) Modify settings.py
- INSTALLED_APPS

4) Modify model.py under app "tour_app"

5) Install Pillow to support ImageField
\travel_proj\travel_proj>pip install pillow

6) Run the below command to create migrations file
\travel_proj\travel_proj>python manage.py makemigration

7) Run the below command to create tables in DB
\travel_proj\travel_proj>python manage.py migrate

8) Modify admin.py under tour_app

9) Test using runserver
\travel_proj\travel_proj>python manage.py runserver

10) On browser, go to admin portal and create records for detainations