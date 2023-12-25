from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
]