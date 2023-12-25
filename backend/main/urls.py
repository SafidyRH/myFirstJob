from django.urls import path
from . import views
from .views import search_jobs


urlpatterns = [
    path("", views.homepage, name="homepage"),    
    path('search/', search_jobs, name='search_jobs'),
]
