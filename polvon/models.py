from django.db import models
from decimal import Decimal
from django import forms
from phonenumber_field.modelfields import PhoneNumberField
import random
import string
import uuid
from datetime import datetime
# from user.models import *



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['my_order']
        verbose_name = 'category'
        verbose_name_plural = "categories"


class Product(BaseModel):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    stock = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    # likes = models.ManyToManyField(User, related_name='likes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_absolute_url(self):
        image = self.product_images.filter(is_primary=True).first()
        if image:
            return image.image.url
        return None

    @property
    def discounted_price(self):
        self.new_price = self.price
        if self.discount > 0:
            self.new_price = Decimal(self.price) * Decimal((1 - self.discount / 100))
        return Decimal(self.new_price).quantize(Decimal('0'))

    def __str__(self):
        return self.name

    def average_rating(self):
        comments = self.comments.all()
        if comments:
            return sum(comment.rating for comment in comments) / len(comments)
        return 0

    class Meta:
        ordering = ['my_order']
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Image(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='product_images', null=True,
                                blank=True)
    image = models.ImageField(upload_to='media/products/', null=True, blank=True)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.image} => {self.is_primary}'


class Attribute(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='product_attributes', null=True,
                                blank=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.SET_NULL, null=True, blank=True)
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.attribute.name


class Comment(BaseModel):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    rating = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.product.name} ({self.rating}⭐)"

    class Meta:
        ordering = ['-created_at']


