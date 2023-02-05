from django.contrib import admin
from .models import ProductModel, CategoryModel, BrandModel, TagModel, SizeModel, ColorModel, ProductImagesModel
from .forms import AddColorForm
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'real_price', 'price', 'discount', 'sale']
    list_display_links = ['id', 'title', 'real_price', 'price', 'discount']
    search_fields = ['title']
    list_filter = ['created_at']
    readonly_fields = ['real_price', 'sale']



@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['created_at']



@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']



@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']



@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'size']
    list_display_links = ['id', 'size']
    search_fields = ['size']



@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'show_color']
    list_display_links = ['id', 'code']
    form = AddColorForm

    def show_color(self, obj):
        return mark_safe(f"<div style='background-color: {obj.code}; width: 100px; height: 20px;'></div>")
    
admin.site.register(ProductImagesModel)