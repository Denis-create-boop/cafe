from django.contrib import admin
from django.urls import path

from dishes import views

app_name = "dishes"

urlpatterns = [
    path("", views.catalog, name="index"),
    path("product/", views.product, name="product"),
]
