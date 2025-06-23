from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """ Wishlist admin """
    list_display = ['user']
    search_fields = ['user__username']
    readonly_fields = ['created_at', 'updated_at']
    

