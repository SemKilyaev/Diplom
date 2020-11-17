from django.urls import path
from . import views

urlpatterns = [
    path('weather', views.index, name='weather'),
    path('/delete/<str:pk>/', views.deleteCity, name='delete'),
    ]