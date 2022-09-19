from django.db import models
from apps.catalog.models import Product
from apps.user.models import User


class Cart(models.Model):
    product = models.ForeignKey(to=Product, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Колличество товара', default=1)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
