from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION


# Ensure STATICFILES_LOCATION and MEDIAFILES_LOCATION are defined in settings
assert hasattr(
    settings,
    'STATICFILES_LOCATION'), "STATICFILES_LOCATION is not defined in settings"
assert hasattr(
    settings,
    'MEDIAFILES_LOCATION'), "MEDIAFILES_LOCATION is not defined in settings"
