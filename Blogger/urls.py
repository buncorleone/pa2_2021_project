from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.index),
    path('myposts/', views.my_posts, name='my_posts'),
    path('posts/', views.Posts.as_view(), name='posts'),
    path('categories/', views.Categories.as_view(), name='categories'),
    path('register/', views.Register.as_view(), name='register_user'),
    path('login/', TokenObtainPairView.as_view(), name='login_user'),
    path('refreshlogin', TokenRefreshView.as_view(), name='refresh_login'),
]