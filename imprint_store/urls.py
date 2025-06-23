from django.contrib import admin
from django.urls import path, include , re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from imprint_store.views import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
    path('wishlist/', include('wishlist.urls')),


    re_path(r'^favicon\.ico$', RedirectView.as_view(
        url=settings.STATIC_URL + 'favicon.ico', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = handler404
