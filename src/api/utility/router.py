from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter


def get_router():
    if settings.DEBUG:
        router = DefaultRouter(trailing_slash=False)
    else:
        router = SimpleRouter(trailing_slash=False)
    return router
