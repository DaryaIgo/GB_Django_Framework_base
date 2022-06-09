from django.urls import path

from basketapp.views import basket_add, basket_list, basket_remove, basket_edit


app_name = 'basket'

urlpatterns = [
    path('', basket_list, name='list'),
    path('add/<pk>/', basket_add, name='add'),
    path('remove/<pk>/', basket_remove, name='remove'),
    path('edit/<pk>/<quantity>/', basket_edit, name='edit'),

]