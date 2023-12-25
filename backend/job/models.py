from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()
    # Autres champs d'entreprise

class JobListing(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True)
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    # Autres champs d'offre d'emploi

class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    job = models.ForeignKey(JobListing, on_delete=models.SET_NULL, null=True)
    cover_letter = models.TextField()
    application_status = models.CharField(max_length=20, choices=[
        ('pending', 'En attente'),
        ('accepted', 'Acceptée'),
        ('rejected', 'Refusée'),
    ])
    # Autres champs de candidature