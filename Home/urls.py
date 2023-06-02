from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('create_result/<int:pk>/', views.TestResultCreateView.as_view(), name='create_result'),

]

