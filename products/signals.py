from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .models import ProductModel


@receiver(pre_save, sender=ProductModel)
def real_price(sender, instance, **kwargs):
        if instance.is_discount:
            instance.real_price = instance.price - (instance.price * instance.discount) / 100
            return instance.real_price
        instance.real_price = 0
        return instance.real_price


@receiver(pre_save, sender=ProductModel)
def set_sale(sender, instance, *args, **kwargs):
    if instance.is_discount():
        instance.sale = True
    else:
        instance.sale = False