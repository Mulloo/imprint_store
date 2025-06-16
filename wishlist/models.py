from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Wishlist(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='wishlist'
    )
    products = models.ManyToManyField(Product, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s wishlist"

    def product_names(self):
        return ", ".join([p.name for p in self.products.all()])
    product_names.short_description = "Products"
