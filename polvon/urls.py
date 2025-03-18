from django.contrib import admin
from django.urls import path , include
from polvon import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('detail/', views.details , name='detail'),
    path('comment-list/' , views.CommentListCreateView.as_view(), name='comment-list'),
    path('comment-detail/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
]