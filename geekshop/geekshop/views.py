from random import randint     # [randint(0, 3)]

from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title = 'GeekShop'
    products = Product.objects.all()[:3]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'Contacts'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/contacts.html', context)
