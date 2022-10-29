from django.contrib import admin
from django.urls import path, include

from apps.post.views import add, notice

app_name= 'post'


urlpatterns = [
    path('add/', add, name='add'),
    path('notice/', notice, name='notice'),
]
