from django.shortcuts import render

from  dishes.models import Categories


def index(request):

    context = {
        "title": "Little Italy - Главная", 
        "content": "Кафе - Little Italy",
        }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Little Italy - О нас",
        "content": "О нас",
        "text_on_page": "hgdg gvydgy gsguy gigkdgv gvdg fdjhdjhjkh dfkjvkfdj fvjdbvj fjvhfjdh fbvjbfdkb fvbkfbvk jbvjbdfj fvkfb",
    }
    return render(request, "main/about.html", context)
