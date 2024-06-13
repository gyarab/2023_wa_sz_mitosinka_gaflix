from django.contrib import admin
from django.urls import path

from filmy import views

urlpatterns = [
    path('', views.index, name='index'),
]
