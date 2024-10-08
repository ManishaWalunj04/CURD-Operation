from django.contrib import admin
from django.urls import path, include
from . import views
from .views import edit_emp_profile

urlpatterns = [
    path('', views.index, name='index'),
    path('all_emp/', views.all_emp, name='all_emp'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('remove_emp/', views.remove_emp, name='remove_emp'),
    path('remove_emp/<int:id>/', views.remove_emp, name='remove_emp'),
    path('filter_emp/', views.filter_emp, name='filter_emp'),
    path('users/<int:id>/', edit_emp_profile, name='edit-user-profile'),

]