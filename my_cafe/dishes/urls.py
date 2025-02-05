from django.contrib import admin
from django.urls import path

from dishes import views

app_name = "dishes"

urlpatterns = [
    path("search/", views.catalog, name="search"),
    path("<slug:category_slug>/", views.catalog, name="index"),
    path("product/<slug:product_slug>/", views.product, name="product"),
]
