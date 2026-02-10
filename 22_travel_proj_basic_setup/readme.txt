Use PyCharm to create a project, with project name as travel_proj

1) Once project loaded, open Terminal and input below command

\travel_proj>pip install django
\travel_proj>django-admin startproject travel_proj
\travel_proj>cd travel_proj
\travel_proj\travel_proj>python manage.py startapp public_app
\travel_proj\travel_proj>pip freeze > requirements.txt

2) Create the following folders under project folder
* Project Folder means the folder that contain manage.py

- media
- templates
- static
  |- css
  |- img
  |- js

3) Create the following folders under app "public_app"

- templates
  |-public_app
- static
  |-public_app
    |- css
    |- img
    |- js

4) Create base.html under project_folder-->templates

5) Create index.html, about.html under app_folder-->templates-->public_app

6) Modify views.py under public_app

7) Create urls.py under public_app

8) Modify urls.py under travel_proj

9) Modify settings.py under travel_proj
- INSTALLED_APPS
- TEMPLATES
- SATAICFILES_DIRS
- STATIC_ROOT
- MEDIA_ROOT
- MEDIA_URL

10) Run the below command to create tables in DB
\travel_proj\travel_proj>python manage.py migrate

11) Run the below command to create first user
\travel_proj\travel_proj>python manage.py createsuperuser

12) Test using runserver
\travel_proj\travel_proj>python manage.py runserver

13) Consolidate static resources to single directory for production deployment
\travel_proj\travel_proj>python manage.py collectstatic