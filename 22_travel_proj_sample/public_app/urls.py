from django.urls import path
from . import views

app_name = 'public_app'

urlpatterns = [
    path('', views.index, name='index'),
]