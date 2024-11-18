from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Cliente'),
        ('seller', 'Vendedor'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    def __str__(self) -> str:
        return super().__str__()
