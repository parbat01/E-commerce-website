from django.urls import path

from shop import views

urlpatterns = [
    path("", views.index, name="shophome"),
    path("about/", views.about, name="aboutus"),
    path("contact/", views.contact, name="contact"),
    path("tracker/", views.tracker, name="tracker"),
    path("search/", views.search, name="search"),
    path("checkout/", views.checkout, name="checkout"),
    path("productview/", views.productview, name="productview"),
]
