from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class User(AbstractUser):
    
    ROLE_CHOICES = (
        ('Employer', 'Recruteur'),
        ('job_seeker', 'Chercheur d\'emploi'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # Il est préférable de stocker le mot de passe haché
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='job_seeker')

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="custom_user_set",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="custom_user_set",
        related_query_name="user",
    )

    def __str__(self):
        return self.username
    
    # Autres champs utilisateur

