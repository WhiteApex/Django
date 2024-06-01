from django.http import HttpResponse
from django.shortcuts import render

#такие функции называются "контроллеры" или "представление"
def index(request):
    contex = {
        'title': 'Home',
        'content': 'Главная страница магазина',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': True

    }
    return render(request, 'main/index.html', contex)

def about(request):
    return HttpResponse('About home')