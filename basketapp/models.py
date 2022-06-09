from django.db import models
from django.conf import settings

from mainapp.models import Product


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')

    def __str__(self):
        return f'{self.product}, {self.quantity}'

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
        ordering = ('created_at', )

    @property
    def product_cost(self):
        return self.product.price

    @property
    def total_quantity(self):
        _item = Basket.objects.filter(user=self.user)
        return sum(list(_item.values_list('quantity', flat=True)))

    @property
    def _total_cost(self):
        _item = Basket.objects.filter(user=self.user)
        return sum(list(map(lambda x: x.product_cost, _item)))
