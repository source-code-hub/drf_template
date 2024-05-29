from django.urls import re_path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    re_path(r'v1/', include('api.users.urls')),
]

urlpatterns.append(re_path(r'^docs/', include_docs_urls(title='API Reference document',
                                                        description='',
                                                        public=True)))
