

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register, name='register'),

    path('my_login', views.my_login, name='my-login'),

    path('dashboard', views.dashboard, name='dashboard'),

    path('user-logout', views.user_logout, name='user-logout'),

    path('profile-management', views.profile_management, name='profile-management'),

    path('delete-account', views.delete_account, name='delete-account'),
]
