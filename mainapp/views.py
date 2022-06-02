from django.shortcuts import render
from mainapp.models import Product, Category


def index(request):

    context = {
        'products': Product.objects.all()[:4]
    }
    return render(request, 'mainapp/index.html')


def products(request):
    context = {
        'links_menu': Category.objects.all()
    }

    return render(request, 'mainapp/products.html', context)

def products_list(request, pk):
    context = {
        'links_menu': Category.objects.all()
    }
    return render(request, 'mainapp/products.html', context)

def contact(request):
    return render(request, 'mainapp/contact.html')

