from django.contrib import admin
from django.urls import path
from .views import home, dashboard,contact

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('contact/', contact, name='contact')
]
