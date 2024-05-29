from django.contrib import admin
from django.urls import path

from django.urls import re_path
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns.append(re_path(r'^docs/', include_docs_urls(title='API Reference document',
                                                        description='',
                                                        public=True)))
