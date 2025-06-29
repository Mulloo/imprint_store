from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_products, name="products"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
    path("add/", views.add_product, name="add_product"),
    path("edit/<int:product_id>/", views.edit_product, name="edit_product"),
    path("delete/<int:product_id>/", views.delete_product, name="delete_product"),
    path("tag/<slug:tag_slug>/", views.product_list_by_tag, name="product_list_by_tag"),

    # Review URLs - fixed parameter names
    path('<int:product_id>/review/add/', views.ReviewCreateView.as_view(), name='add_review'),
    path('<int:product_id>/review/<int:pk>/edit/', views.ReviewUpdateView.as_view(), name='edit_review'),
    path('<int:product_id>/review/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='delete_review'),
]

