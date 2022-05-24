from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):

    links_menu = [
        {'href': 'products_all', 'title': 'все'},
        {'href': 'products_home', 'title': 'дом'},
        {'href': 'products_office', 'title': 'офис'},
        {'href': 'products_modern', 'title': 'модерн'},
        {'href': 'products_classic', 'title': 'классика'},
    ]

    context = {
        'links_menu': links_menu
    }

    return render(request, 'mainapp/products.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')

