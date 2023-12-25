from django.shortcuts import render
from django.http import HttpResponse
from .models import Company, JobListing, JobApplication 

# Create your views here.
def jobs(request):
    return HttpResponse('This is our jobs page, It works!!')