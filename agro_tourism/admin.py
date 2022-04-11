from django.contrib import admin

from .models import Farm, Package

class PackageInline(admin.TabularInline):
    model = Package
    extra = 0
    fields = ['name', 'features', 'pricing', 'images']


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    fields = ['name', 'owner', 'location', 'area', 'contact', 'features', 'images', 'publish']
    inlines = [PackageInline]

