from django.contrib import admin
from django.urls import path , include
from polvon import views

urlpatterns = [
    # path('home/', views.home, name='home'),
    # path('detail/', views.details , name='detail'),
    path('comment-list/' , views.CommentListCreateView.as_view(), name='comment-list'),
    path('comment-detail/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    path('time-district/<int:pk>' , views.TimeDistrictView.as_view(), name='time-district'),
    path('day-district/' , views.DistrictView.as_view(), name='day-district'),
    path('product-list/' , views.ProductView.as_view(), name='product_list'),
]