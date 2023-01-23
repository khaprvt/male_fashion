from django.contrib import admin
from .models import BannerModel,ContactModel

# Register your models here.

@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'collection']
    list_filter = ['created_at']
    

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_display_links = ['name', 'email']
    search_fields = ['name', 'email', 'massage']
    list_filter = ['created_at']