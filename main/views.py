from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

#такие функции называются "контроллеры" или "представление"
def index(request):
    categories = Categories.objects.all()
    contex = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories
    }
    return render(request, 'main/index.html', contex)


def about(request):
    contex = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о товареТекст о товареТекст о товареТекст о товареТекст о товареТекст о товаре'
    }
    return render(request, 'main/about.html', contex)
