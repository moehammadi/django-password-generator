from django.urls import path, include
from generator import views

urlpatterns = [
    path('', views.home, name='home'),
    path('password/', views.password, name='password'),
]
