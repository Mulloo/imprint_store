from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import ProductForm, ReviewForm
from .mixins import ReviewAuthorRequiredMixin
from .models import Category, Product, ProductReview, Tag


def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    user_wishlist_products = []

    # Get user's wishlist if authenticated
    if request.user.is_authenticated:
        try:
            from wishlist.models import Wishlist

            wishlist = Wishlist.objects.get(user=request.user)
            user_wishlist_products = list(
                wishlist.products.values_list("id", flat=True)
            )
        except Wishlist.DoesNotExist:
            pass

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
        "user_wishlist_products": user_wishlist_products,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)

    reviews = product.reviews.filter(approved=True)

    review_form = ReviewForm()

    context = {
        "product": product,
        "reviews": reviews,
        "review_form": review_form,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """Add a product to the store"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to add product. Please ensure the form is valid."
            )
    else:
        form = ProductForm()
    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Successfully updated {product.name}")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to update product. Please ensure the form is valid."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))


def product_list_by_tag(request, tag_slug):
    """A view to show all products by tag"""

    tag = get_object_or_404(Tag, slug=tag_slug, is_active=True)
    products = Product.objects.filter(tags=tag)

    context = {
        "tag": tag,
        "products": products,
    }

    return render(request, "products/products_by_tag.html", context)


class ReviewCreateView(CreateView):
    model = ProductReview
    form_class = ReviewForm
    template_name = "products/reviews/review_form.html"  # Consistent template path

    def dispatch(self, request, *args, **kwargs):
        self.product = get_object_or_404(
            Product, pk=kwargs["product_id"]
        )  # Changed from "pk" to "product_id"
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product = self.product
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class ReviewUpdateView(ReviewAuthorRequiredMixin, UpdateView):
    model = ProductReview
    form_class = ReviewForm
    template_name = "products/reviews/review_form.html"

    def get_success_url(self):
        return self.object.get_absolute_url()


class ReviewDeleteView(ReviewAuthorRequiredMixin, DeleteView):
    model = ProductReview
    template_name = "products/reviews/review_confirm_delete.html"  # Fixed path

    def get_success_url(self):
        return self.object.product.get_absolute_url()
