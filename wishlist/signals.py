from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Wishlist


@receiver(post_save, sender=User)
def create_wishlist(sender, instance, created, **kwargs):
    """ Create a wishlist for new users """
    if created:
        Wishlist.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_wishlist(sender, instance, **kwargs):
    """ Save the wishlist for existing users """
    instance.wishlist.save()
