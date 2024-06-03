from django.http import HttpResponse
from django.shortcuts import render


#такие функции называются "контроллеры" или "представление"
def index(request):
    contex = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }
    return render(request, 'main/index.html', contex)


def about(request):
    contex = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о товареТекст о товареТекст о товареТекст о товареТекст о товареТекст о товаре'
    }
    return render(request, 'main/about.html', contex)
