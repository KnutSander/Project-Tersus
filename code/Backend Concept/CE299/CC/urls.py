#links
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('viewdatabase/', views.viewdatabase.index, name='viewdatabase'),
    path('newuser/', views.newuser.createuser, name='newuser')
]
