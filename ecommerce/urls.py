from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shop", views.contact, name="shop_grid"),
    path("details", views.contact, name="shop_details"),
    path("cart", views.contact, name="cart"),
    path("checkout", views.contact, name="checkout"),
    path("blog", views.blog, name="blog"),
    path("blog_details", views.contact, name="blog_details"),
    path("contact", views.contact, name="contact"),
]
