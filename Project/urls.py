from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import handler404
from core import handlers


handler404 = handlers.handle_not_found_404

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),  # Translate Provider
    url(r"^", include("core.urls", namespace="core"))
]
# print(staticfiles_urlpatterns())
# urlpatterns += staticfiles_urlpatterns()
