#!/usr/bin/env python
# File Name: urls.py
# Author: Amit Singh


from django.urls import re_path, include

from api.utility.router import get_router

# Create a router and register our view sets with it.
router = get_router()
# router.register(r'users', UserViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls))
]
