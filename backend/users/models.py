from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    ROLE_CHOICES = (
        ('Employer', 'Recruteur'),
        ('job_seeker', 'Chercheur d\'emploi'),
    )

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # Il est préférable de stocker le mot de passe haché
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='job_seeker')

    def __str__(self):
        return self.username
    
    # Autres champs utilisateur

