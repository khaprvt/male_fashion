from django.contrib import admin
from .models import BannerModel

# Register your models here.

@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status']
    list_display_links = ['id', 'title']