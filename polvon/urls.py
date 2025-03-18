from django.contrib import admin
from django.urls import path , include
from polvon import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('detail/', views.details , name='detail'),
]