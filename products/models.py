from django.db import IntegrityError, models
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
import datetime

from users.models import UserModel

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
    sale = models.BooleanField(default=False)
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
    
    @staticmethod
    def get_cart_objects(cart_list):
        # [2, 1, 3]
        qs = ProductModel.objects.all().filter(id__in=cart_list)
        return qs
    
    def is_discount(self):
        return bool(self.discount)
    
    def is_new(self):
        return (timezone.now() - self.created_at).days <= 3
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('-id',)


class WishlistModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.RESTRICT)
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.product} {self.user}"
    
    @staticmethod
    def create_or_delete(user, product):
        try:
            WishlistModel.objects.create(user=user, product=product)
        except IntegrityError:
            WishlistModel.objects.get(user=user, product=product).delete()

    class Meta:
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'
        unique_together = ('user', 'product')
        
        
        
class ProductImagesModel(models.Model):
    product = models.OneToOneField(ProductModel, on_delete=models.CASCADE, related_name='images')
    image_1 = models.ImageField(upload_to='product_images/')
    image_2 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image_4 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image_5 = models.FileField(upload_to='product_files/', null=True, blank=True)


    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'