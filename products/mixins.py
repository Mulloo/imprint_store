# products/mixins.py
from django.core.exceptions import PermissionDenied

class ReviewAuthorRequiredMixin:
    """Only the original author (or superuser) may edit / delete."""
    def dispatch(self, request, *args, **kwargs):
        review = self.get_object()
        if request.user == review.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied
