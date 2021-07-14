from .views import *
from django.urls import path


urlpatterns = [
    path('',home,name='base'),
    path('home',home,name='home'),
    path('projects',projects,name='projects'),
    path('education',education,name='education')
]