from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, Category


def get_basket(user):
    basket_list = 0
    if user.is_authenticated:
        basket_list = sum(list(Basket.objects.filter(user=user).values_list('quantity', flat=True)))

    return basket_list


def index(request):
    context = {
        'products': Product.objects.all()[:4],
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    links_menu = Category.objects.all()

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category_item = {'name': 'все', 'pk': 0}
        else:
            category_item = get_object_or_404(Category, pk=pk)
            products_list = Product.objects.filter(category_id=pk)

        context = {
            'links_menu': links_menu,
            'products': products_list,
            'category': category_item,
            'basket': get_basket(request.user)
        }

        return render(request, 'mainapp/products_list.html', context)

    context = {
        'links_menu': links_menu,
        'basket': get_basket(request.user),
        'hot_product': Product.objects.all().order_by('?').first(),
        'same_products': Product.objects.all().order_by('?')[3:5]
    }

    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/contact.html')
