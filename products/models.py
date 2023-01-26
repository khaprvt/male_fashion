from django.db import models
from django.utils import timezone
from datetime import timedelta
import datetime

# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
        
class BrandModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class TagModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        

class SizeModel(models.Model):
    size = models.CharField(max_length=8)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'
        
        
class ColorModel(models.Model):
    code = models.CharField(max_length=7)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'
        
        


class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    long_description = models.TextField()
    price = models.FloatField()
    real_price = models.FloatField(default=0)
    discount = models.PositiveIntegerField(default=0)
    main_image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name='products')
    tag = models.ManyToManyField(TagModel, related_name='products')
    color = models.ManyToManyField(ColorModel, related_name='products')
    size = models.ManyToManyField(SizeModel, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # def real_price(self):
    #     if self.discount:
    #         return self.price - (self.price * self.discount) / 100
    #     return self.price
    
    def is_discount(self):
        return self.discount != 0
    
    def is_new(self):
        return (timezone.now() - self.created_at).days <= 3
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('-id',)
