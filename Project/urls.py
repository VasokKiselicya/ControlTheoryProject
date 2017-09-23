import django
from django.conf.urls import url, include, i18n
from django.contrib import admin
from core import handlers

setattr(django.conf.urls, "handler404", handlers.handle_not_found_404)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include(i18n)),  # Translate Provider
    url(r"^", include("core.urls", namespace="core"))
]
