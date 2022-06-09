from django.contrib import admin

from basketapp.models import Basket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'quantity',)
    list_filter = ('product', )

    def total_price(self, obj):
        return obj.product.price * obj.quantity
