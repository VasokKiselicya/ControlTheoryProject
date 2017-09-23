from django.conf.urls import url, include

urlpatterns = [
    url(r"^", include("account.urls", namespace="auth"))
]
