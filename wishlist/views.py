from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from products.models import Product

from .models import Wishlist


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    if product in wishlist.products.all():
        messages.info(request, f"{product.name} is already in your wishlist.")
    else:
        wishlist.products.add(product)
        messages.success(request, f"Added {product.name} to your wishlist.")

    return redirect(request.META.get("HTTP_REFERER", "wishlist:view_wishlist"))


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request, f"Removed {product.name} from your wishlist.")
    else:
        messages.warning(request, f"{product.name} was not in your wishlist.")

    return redirect(request.META.get("HTTP_REFERER", "wishlist:view_wishlist"))


@login_required
def view_wishlist(request):
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    products = wishlist.products.all()
    return render(
        request,
        "wishlist/view_wishlist.html",
        {"wishlist": wishlist, "products": products},
    )
