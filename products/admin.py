from django.contrib import admin
from .models import Category, Product, Inventory

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'name',
    )

class InventoryAdmin(admin.ModelAdmin):  # Create an admin class for Inventory
    list_display = (
        'product',
        'in_stock',
        'last_updated',
    )

    ordering = ('product',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Inventory, InventoryAdmin) 
