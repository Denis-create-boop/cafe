from django.shortcuts import render

from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Little Italy - Каталог",
    }
    return render(request, "dishes/catalog.html", context)


def product(request):
    return render(request, "dishes/product.html")
