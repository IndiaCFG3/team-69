from django.contrib import admin
from django.urls import path
from .views import home, dashboard

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard')
]
