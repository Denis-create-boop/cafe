from django.shortcuts import render

from  dishes.models import Categories


def index(request):

    dishes = Categories.objects.all()

    context = {
        "title": "Little Italy - Главная", 
        "content": "Кафе - Little Italy",
        "dishes": dishes
        }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Little Italy - О нас",
        "content": "О нас",
        "text_on_page": "hgdg gvydgy gsguy gigkdgv gvdg fdjhdjhjkh dfkjvkfdj fvjdbvj fjvhfjdh fbvjbfdkb fvbkfbvk jbvjbdfj fvkfb",
    }
    return render(request, "main/about.html", context)
