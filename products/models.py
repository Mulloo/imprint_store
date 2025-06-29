from crum import get_current_request
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, unique=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254,  unique=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    tags = models.ManyToManyField(
        'Tag',
        related_name='products',
        verbose_name='Tags',
        help_text='format: required, max_length=100'
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Tag model"""
    name = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        blank=False,
        verbose_name='Tag name',
        help_text='format: required, max_length=100'
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        unique=True,
        blank=False,
        verbose_name='Tag Slug',
        help_text='format: required, max_length=150'
    )
    is_active = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated at'
    )

    class Meta:
        """Meta class for Tag model"""
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def __str__(self):
        """String representation of Tag model"""
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    @classmethod
    def get_active_tags(cls):
        """Get active tags"""
        return cls.objects.filter(is_active=True)

    @classmethod
    def get_not_active_tags(cls):
        """Get not active tags"""
        return cls.objects.filter(is_active=False)

class ProductReview(models.Model):
    """Product Review model"""

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product.id]) + '#reviews'

    def is_owner(self):
        from django.contrib.auth import get_user
        request = get_current_request()
        return request and request.user == self.user
    class Rating(models.IntegerChoices):
        ONE   = 1, _("★☆☆☆☆")
        TWO   = 2, _("★★☆☆☆")
        THREE = 3, _("★★★☆☆")
        FOUR  = 4, _("★★★★☆")
        FIVE  = 5, _("★★★★★")     
    
    product = models.ForeignKey(
        'products.Product',
        related_name='reviews',
        on_delete=models.CASCADE)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='reviews',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=Rating.choices)
    created_at = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('product', 'user')
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.product.name} - {self.user.username}'