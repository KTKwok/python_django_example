from django.urls import path
from . import views

app_name = 'tour_app'

urlpatterns = [
    path("", views.landing, name="landing"),
    path("destination/<int:id>", views.destination, name="get_destination"),
]