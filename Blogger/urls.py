from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('myposts/', views.my_posts),
    path('posts/', views.list_posts),
    path('categories/', views.list_categories),
]