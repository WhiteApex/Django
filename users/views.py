from django.shortcuts import render


# Create your views here.
def login(request):
    contex = {
        'title': 'Home - Авторизация',
    }
    return render(request, 'users/login.html', contex)


def registration(request):
    contex = {
        'title': 'Home - Регистрация',
    }
    return render(request, 'users/registration.html', contex)


def profile(request):
    contex = {
        'title': 'Home - Кабинет',
    }
    return render(request, 'users/profile.html', contex)


def logout(request):
    contex = {
        'title': 'Home - Авторизация',
    }
    return render(request, '', contex)