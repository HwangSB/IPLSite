from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.redirect_home, name='redirect_home'),
    path('home/', views.home, name='home'),
    path('members/', views.members, name='members'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
]
