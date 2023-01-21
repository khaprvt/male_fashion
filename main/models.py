from django.db import models

# Create your models here.

class BannerModel(models.Model):
    collection = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner_image = models.ImageField(upload_to='banners/')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'