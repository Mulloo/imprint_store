from django.contrib import admin
from .models import Product, Category, Tag


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """ Tag Admin """
    list_display = ('name', 'slug', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
