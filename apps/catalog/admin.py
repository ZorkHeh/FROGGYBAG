from django.contrib import admin
from apps.catalog.models import Category, Product, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


class ProductCategoryInline(admin.TabularInline):
    model = Product.categories.through
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = Product.images.through
    extra = 1


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'quantity', 'price']
    inlines = [ProductCategoryInline, ProductImageInline]
