"""
Signals to create and update UserProfile records based
on their associated CustomUser records.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser, UserProfile

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    """
    Create a UserProfile record when a new CustomUser is created.
    """
    if created:
        UserProfile.objects.create(player=instance)

@receiver(post_save, sender=CustomUser)
def update_profile(sender, instance, created, **kwargs):
    """
    Update a UserProfile record when its associated
    CustomUser instance is updated.
    """
    if created is False:
        instance.playerprofile.save()
