from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jobs(request):
    return HttpResponse('This is our jobs page, It works!!')