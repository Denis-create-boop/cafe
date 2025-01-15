from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator

from dishes.models import Products


def catalog(request, category_slug):

    dishes = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(dishes, 3)
    current_page = paginator.page(1)

    context = {
        "title": "Little Italy - Каталог",
        "dishes": current_page,
    }
    return render(request, "dishes/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, "dishes/product.html", context=context)