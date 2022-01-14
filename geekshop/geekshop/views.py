from random import randint     # [randint(0, 3)]

from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    title = 'GeekShop'
    products = Product.objects.all()[:3]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'products': products,
        'basket': basket,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'Contacts'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'geekshop/contacts.html', context)
