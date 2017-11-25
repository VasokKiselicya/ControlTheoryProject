from django.conf.urls import url
from core.service import views

urlpatterns = [
    url(r"^menu/", views.MenuView.as_view(), name='show-menu'),
    url(r"^restaurant/", views.RestaurantView.as_view(), name='restaurant'),
    url(r"^contacts/", views.ContactsView.as_view(), name='contacts'),
    url(r"^blog/(?P<slug>(.*))/$", views.ArticleView.as_view()),
    url(r"^blog/$", views.BlogView.as_view(), name="blog"),
    url(r"^cart-control/$", views.CartControl.as_view(), name="cart-control"),
    url(r"^basket/$", views.CartView.as_view(), name="basket")
]
