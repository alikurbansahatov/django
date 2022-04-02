from django.contrib import admin
from django.urls import path
from first_app import views
from django.conf.urls import include
urlpatterns = [
    path('page1/', views.page1, name='Page1'),
    ]