mkdir proj
cd proj
python -m venv .venv
.venv\Scripts\activate
pip freeze > requirements.txt
pip install django
pip freeze > requirements.txt
django-admin startproject proj .
python manage.py runserver