from django.contrib import admin
from blog.models import BlogPost

@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'author', 'publish', 'status'
    )
    list_filter = (
        'status', 'created', 'publish', 'author'
    )
    search_fields = (
        'title', 'body'
    )
    raw_id_fields = (
        'author',
    )
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')