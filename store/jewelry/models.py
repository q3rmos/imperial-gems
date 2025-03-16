from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Category Name")
    slug = models.SlugField(unique=True, verbose_name="Category Slug")
    image = models.ImageField(
        upload_to="categories/",
        blank=True,
        null=True,
        verbose_name="Category Image",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product Name")
    slug = models.SlugField(
        unique=True, blank=True, null=True, verbose_name="Product Slug"
    )
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    image = models.ImageField(
        upload_to="products/", blank=True, null=True, verbose_name="Product Image"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Category",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class CartItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Product"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.quantity * self.product.price

    class Meta:
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"


class Order(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Customer Email")
    phone = models.CharField(max_length=15, verbose_name="Phone")

    country = models.CharField(max_length=100, verbose_name="Country")
    region = models.CharField(max_length=100, verbose_name="Region/State")
    city = models.CharField(max_length=100, verbose_name="City")
    postal_code = models.CharField(max_length=20, verbose_name="Postal Code")

    address = models.TextField(verbose_name="Shipping Address")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.full_name}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderItem(models.Model):
    order = models.ForeignKey(
        "Order", on_delete=models.CASCADE, related_name="order_items"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
