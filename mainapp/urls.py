from django.urls import path
from mainapp.views import products, products_list

app_name = 'products'

urlpatterns = [
    path('', products, name='products_hot_product'),
    path('<int:pk>/', products_list, name='product_list',)
]
