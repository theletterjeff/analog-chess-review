from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """The auth_user model."""
    pass

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    """Profile information for CustomUser instances."""
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username
