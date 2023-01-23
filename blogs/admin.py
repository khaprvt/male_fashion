from django.contrib import admin
from .models import BlogModel, BlogTagsModel, CommentModel

# Register your models here.

@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['created_at']
    

@admin.register(BlogTagsModel)
class BlogTagsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    

@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'created_at']
    list_display_links = ['name', 'comment', 'created_at']
    readonly_fields = ['name', 'email', 'phone', 'comment']