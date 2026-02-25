from django.urls import path
from . import views

app_name = 'public_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('organization/', views.company_org_chart, name='company_org_chart'),
]