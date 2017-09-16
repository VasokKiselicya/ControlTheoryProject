from django.conf.urls import url
from core.landing.views import LandingView


urlpatterns = [
    url(r"^$", LandingView.as_view())
]
