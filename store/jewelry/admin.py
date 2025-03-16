from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Category, Product, CartItem, Order, CustomUser

admin.site.site_header = "Imperial Gems Control Panel"
admin.site.site_title = "Imperial Gems | Admin"
admin.site.index_title = "Welcome to the admin panel"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "email", "phone", "is_staff", "is_active"]
    search_fields = ["username", "email", "phone"]
    list_editable = ["is_staff", "is_active"]
    list_filter = ["is_superuser", "is_active"]
    fieldsets = (
        ("Personal Info", {"fields": ("username", "email", "phone", "address")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            "Create User",
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )
    ordering = ["username"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    list_filter = ("category",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "created_at")
    search_fields = ("full_name", "email")
    readonly_fields = ("created_at",)
