from django.urls import path
from mainapp.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='products_hot_product'),
    path('<int:pk>/', products, name='product_list',)
]
