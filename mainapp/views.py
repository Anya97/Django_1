import json

from django.conf import settings
from django.shortcuts import render

# request - all information about what happened on the user's side
from mainapp.models import Product, ProductCategory


def index(request):
    products_list = Product.objects.all()[:4]
    print(products_list.query)

    context = {
        'title': 'Если у вас возникли вопросы, свяжитесь с нами',
        'products': products_list
    }

    return render(request, 'mainapp/index.html', context)


def contact(request):
    with open(f'{settings.BASE_DIR}/contact.json') as contacts_file:
        context = {
            'contacts': json.load(contacts_file)
        }
    return render(request, "mainapp/contact.html", context)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    context = {
        'links_menu': links_menu,
        'title': 'Товары'
    }
    return render(request, "mainapp/products.html", context)
