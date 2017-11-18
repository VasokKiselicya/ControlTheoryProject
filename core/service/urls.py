from django.conf.urls import url
from core.service.views import MenuView, ArticleView, BlogView

urlpatterns = [
    url(r"^menu/", MenuView.as_view()),
    url(r"^blog/(?P<slug>(.*))/$", ArticleView.as_view()),
    url(r"^blog/$", BlogView.as_view(), name="blog")
]
