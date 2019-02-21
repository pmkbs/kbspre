from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display_links =(
        'location',
    )

    search_fields =(
        'location',
    )

    list_filter =(
        'file',
        'location',
        'caption',
        'creator',
        'created_at',
        'updated_at',
    )

    list_display =(
        'file',
        'location',
        'caption',
        'creator',
        'created_at',
        'updated_at',
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display =(
        'creator',
        'image',
        'created_at',
        'updated_at',
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin): 
    list_display =(
        'id',
        'created_at',
        'playername',
        'step',
        'score',
        'tel',
        'mail',
        'survey',
        'note',
        'image',
        'creator',
        'message',
        'updated_at',
    )
