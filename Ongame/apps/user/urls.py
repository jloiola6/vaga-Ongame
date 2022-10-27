from django.contrib import admin
from django.urls import path, include

from apps.user.views import login, logout, register


app_name= 'user'
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
]
