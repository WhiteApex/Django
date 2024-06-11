from django import forms
#Наследуем готовый класс, в котором пропасаны все важные параметры для регистрации
from django.contrib.auth.forms import AuthenticationForm
from users.models import User


#Создаем класс наследник проверки авторизации
class UserLoginForm(AuthenticationForm):
    #Дополняем стандарный класс валидации - связывая его с конкретной моделью в БД
    username = forms.CharField()
    password = forms.CharField()
    #Мы можем кастомизировать html разметку через свойства формы
    #Но это не правильный подход, потому что нагружает бекэнд
    # username = forms.CharField(
    #     label='Имя',
    #     widget=forms.TextInput(
    #     attrs={"autofocus": True,
    #            'class': 'form-control',
    #            'placeholder': "Введите ваше имя пользователя",
    #            }))
    # password = forms.CharField(
    #     label='Пароль',
    #     widget=forms.PasswordInput(
    #         attrs={"autocomplete": "current-password",
    #                'class': 'form-control',
    #                'placeholder': "Введите ваш пароль",
    #                }),
    # )

    class Meta:
        model = User
        fields = ['username', 'password']