from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("product/", views.product, name = "Product"),
    path("upload/", views.upload, name = "Upload")
]