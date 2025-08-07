from django.contrib import admin
from django.contrib.admin import register
from package.models import Package


@register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ["title", "price"]
