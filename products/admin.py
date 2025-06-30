from django.contrib import admin

from .models import Category, Product, ProductReview, Tag


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "image",
    )

    ordering = ("sku",)

    filter_horizontal = ("tags",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag Admin"""

    list_display = ("name", "slug", "is_active")

    prepopulated_fields = {"slug": ("name",)}


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating", "approved", "created_at")
    list_filter = ("approved", "rating", "created_at")
    search_fields = ("product__name", "user__username", "title", "content")
    actions = ["approve_selected"]

    @admin.action(description="Mark selected reviews as approved")
    def approve_selected(self, request, queryset):
        queryset.update(approved=True)
