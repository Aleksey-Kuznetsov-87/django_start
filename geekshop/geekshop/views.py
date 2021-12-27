from django.shortcuts import render


def index(request):
    title = 'GeekShop'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'Contacts'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/contacts.html', context)
