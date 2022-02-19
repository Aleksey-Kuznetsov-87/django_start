from django.shortcuts import render
from mainapp.models import Product


def index(request):
    title = 'GeekShop'
    products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:3]

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
