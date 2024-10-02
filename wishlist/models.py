from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    """ Wishlist model """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='wishlist')

    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"{self.user.username}'s wishlist"
