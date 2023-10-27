from django.db import models
from django.contrib.auth.models import User
#from users.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField()
    cv = models.FileField(upload_to='cv/', null=True, blank=True)
    # Autres champs de profil utilisateur
