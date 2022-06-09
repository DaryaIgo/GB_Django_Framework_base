from basketapp.models import Basket
from mainapp.models import Product


def get_basket(user):
    basket_list = 0
    if user.is_authenticated:
        basket_list = Basket.objects.filter(user=user)

    return basket_list


def get_hot_product():
    return Product.objects.all().order_by('?').first()


def get_same_products(product):
    return Product.objects.filter(category=product.category).exclude(pk=product.pk)[:3]

