from django.conf.urls import url
from django.views.generic import TemplateView
from core.service.views import MenuView

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="base.html")),
    url(r"^menu/", MenuView.as_view())
]
