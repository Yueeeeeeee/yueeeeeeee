from django.contrib import admin
from image.models import Image

# Register your models here.

@admin.register(Image)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'title', 'slug', 'description', 'created'
    )
    list_filter = (
        'user', 'created'
    )
    search_fields = (
        'title', 'description', 'created'
    )
    raw_id_fields = (
        'user',
    )
    date_hierarchy = 'created'
    ordering = ('user', 'title')