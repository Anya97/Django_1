import json

from django.conf import settings
from django.shortcuts import render


# request - all information about what happened on the user's side


def index(request):
    context = {
        'title': 'Если у вас возникли вопросы, свяжитесь с нами'
    }

    return render(request, "mainapp/index.html", context)


def contact(request):
    with open(f'{settings.BASE_DIR}/contact.json') as contacts_file:
        context = {
            'contacts': json.load(contacts_file)
        }
    return render(request, "mainapp/contact.html", context)


links_menu = [
    {'href': 'products', 'name': 'Все'},
    {'href': 'products_home', 'name': 'Дом'},
    {'href': 'products_modern', 'name': 'Модерн'},
    {'href': 'products_office', 'name': 'Офис'},
    {'href': 'products_classic', 'name': 'Классика'},
]


def products(request):
    context = {
        'links_menu': links_menu,
        'title': 'Товары'
    }
    return render(request, "mainapp/products.html", context)


def products_home(request):
    context = {
        'links_menu': links_menu,
        'title': 'Товары'
    }
    return render(request, "mainapp/products.html", context)


def products_modern(request):
    context = {
        'links_menu': links_menu,
        'title': 'Товары'
    }
    return render(request, "mainapp/products.html", context)


def products_office(request):
    context = {
        'links_menu': links_menu,
        'title': 'Товары'
    }
    return render(request, "mainapp/products.html", context)


def products_classic(request):
    context = {
        'links_menu': links_menu,
        'title': 'Товары'
    }
    return render(request, "mainapp/products.html", context)
