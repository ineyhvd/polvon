# admin.py
from django.contrib import admin
from .models import Category, Product, Image, Attribute, AttributeValue, ProductAttribute, Comment


# Category modeli uchun admin konfiguratsiyasi
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'my_order', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['title']
    ordering = ['my_order']


# Product modeli uchun admin konfiguratsiyasi
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'discount', 'discounted_price', 'stock', 'favorite', 'created_at']
    list_filter = ['category', 'stock', 'favorite', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['my_order']
    list_per_page = 20

    # Inline modellar
    class ImageInline(admin.TabularInline):
        model = Image
        extra = 1

    class ProductAttributeInline(admin.TabularInline):
        model = ProductAttribute
        extra = 1

    class CommentInline(admin.TabularInline):
        model = Comment
        extra = 1

    inlines = [ImageInline, ProductAttributeInline, CommentInline]


# Image modeli uchun admin konfiguratsiyasi
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image', 'is_primary', 'created_at']
    list_filter = ['is_primary', 'created_at']
    search_fields = ['product__name']


# Attribute modeli uchun admin konfiguratsiyasi
@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


# AttributeValue modeli uchun admin konfiguratsiyasi
@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ['value']
    search_fields = ['value']


# ProductAttribute modeli uchun admin konfiguratsiyasi
@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['product', 'attribute', 'attribute_value']
    list_filter = ['attribute']
    search_fields = ['product__name', 'attribute__name']


# Comment modeli uchun admin konfiguratsiyasi
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'product', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['full_name', 'email', 'product__name']
    ordering = ['-created_at']