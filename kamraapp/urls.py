# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from .static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('kamraapp.apps.bet.urls', namespace='bet')),
]

if settings.DEBUG is True or settings.TEST_PREPROD is True:
    # Add the MEDIA_URL to the dev environment
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
