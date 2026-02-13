from django.urls import path
from . import views

app_name = 'store_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('author/create/',views.create_author,name='create_author'),
    path('author/create/form/',views.create_author_form,name='create_author_form'),
    path('author/get_create/',views.get_or_create_author,name='get_or_create_author'),
    path('author/update/form/<int:pk>/',views.update_author_form,name='update_author_form'),
]