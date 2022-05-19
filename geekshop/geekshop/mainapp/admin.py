from django.contrib import admin

# Register your models here.
from mainapp.models import Product, ProductCategories


admin.site.register(ProductCategories)

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    ordering = ('name', 'price')
    search_fields = ('name',)