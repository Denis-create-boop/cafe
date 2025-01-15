from django.shortcuts import render

from dishes.models import Products


def catalog(request):
    dishes = Products.objects.all()
    context = {
        "title": "Little Italy - Каталог",
        "dishes": dishes,
        
    }
    return render(request, "dishes/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, "dishes/product.html", context=context)
