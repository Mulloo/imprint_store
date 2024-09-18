from django.shortcuts import render 
from .models import Product


# Create your views here.
def all_products(request):
    """ This view to show all products and sorting and searching """
    products = Product.objects.all()

    return render(request, 'products/products.html', context)