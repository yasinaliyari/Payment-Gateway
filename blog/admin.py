from django.contrib import admin
from django.contrib.admin import register
from blog.models import Post


@register(Post)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
    )
