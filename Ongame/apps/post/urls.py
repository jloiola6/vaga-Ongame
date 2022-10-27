from django.contrib import admin
from django.urls import path, include

from apps.post.views import index

app_name= 'post'


urlpatterns = [
    path('', index, name='index')
]
