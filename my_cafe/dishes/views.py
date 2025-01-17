from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator

from dishes.models import Products


def catalog(request, category_slug):

    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)

    dishes = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        dishes = dishes.filter(discount__gt=0)
    if order_by and order_by != "default":
        dishes = dishes.order_by(order_by)

    paginator = Paginator(dishes, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Little Italy - Каталог",
        "dishes": current_page,
        "slug_url": category_slug,
    }
    return render(request, "dishes/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {"product": product}
    return render(request, "dishes/product.html", context=context)
