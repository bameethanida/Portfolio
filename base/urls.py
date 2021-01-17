from django.urls import path
from . import views

app_name = 'Resume'
urlpatterns = [
    path('', views.home, name="home"),
    path('aboutme/', views.aboutme, name="aboutme"),
    path('experiences/', views.experiences, name="experiences"),
    path('project/', views.projects, name="projects"),
    path('activities/', views.activities, name="activities"),
    path('contact/', views.contact, name="contact")
]