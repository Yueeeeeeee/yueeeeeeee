from django.contrib import admin
from blog.models import BlogPost, BlogComment

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

@admin.register(BlogComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'created', 'post', 'active'
    )
    list_filter = (
        'active', 'username', 'email'
    )
    search_fields = (
        'username', 'email', 'post'
    )