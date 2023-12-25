# main/views.py
from django.shortcuts import render
from django.http import HttpResponse
from job.models import JobListing  # Assurez-vous d'importer le modèle JobListing


def homepage(request):
    return render(request,'main/home.html')

"""def search_jobs(request):
    query = request.GET.get('q')
    results = JobListing.objects.filter(job_title__icontains=query)
    return render(request, 'main/search_results.html', {'results': results})"""


def search_jobs(request):
    query = request.GET.get('q')

    if query:
        results = JobListing.objects.filter(job_title__icontains=query)
    else:
        results = []  # Si la requête est vide, initialisez les résultats comme une liste vide

    return render(request, 'main/search_results.html', {'results': results})

