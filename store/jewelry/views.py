from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, CartItem, OrderItem
from .forms import (
    OrderForm,
    ContactForm,
    CustomUserCreationForm,
    CustomAuthenticationForm,
)
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    categories = Category.objects.all()
    popular_products = Product.objects.order_by("?")[:4]
    return render(
        request,
        "jewelry/index.html",
        {"categories": categories, "popular_products": popular_products},
    )


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "❌ Invalid login credentials. Please try again.")
    else:
        form = CustomAuthenticationForm()
    return render(request, "registration/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("home")


def products(request):
    products = Product.objects.all()
    return render(request, "jewelry/products.html", {"products": products})


def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(
        request, "jewelry/category.html", {"category": category, "products": products}
    )


def get_categories(request):
    categories = Category.objects.all()
    return {"categories": categories}


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "jewelry/product_detail.html", {"product": product})


@login_required
def cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.total_price() for item in cart_items)
    return render(
        request,
        "jewelry/cart.html",
        {"cart_items": cart_items, "total_price": total_price},
    )


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)

    if created:
        cart_item.quantity = 1
    else:
        cart_item.quantity += 1

    cart_item.save()
    return redirect("cart")


@login_required
def remove_from_cart(request, product_id):
    cart_item = get_object_or_404(CartItem, product_id=product_id)
    cart_item.delete()
    return redirect("cart")


def update_cart_item(request, product_id):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        cart_item = get_object_or_404(CartItem, product_id=product_id)

        if quantity >= 1:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()

        total_price = sum(item.total_price() for item in CartItem.objects.all())

        return JsonResponse(
            {
                "success": True,
                "quantity": cart_item.quantity,
                "total_price": cart_item.total_price(),
                "cart_total": total_price,
            }
        )

    return JsonResponse({"success": False, "error": "Invalid request"})


@login_required
def clear_cart(request):
    CartItem.objects.all().delete()
    messages.success(request, "Cart successfully emptied!")
    return redirect("cart")


def checkout(request):
    cart_items = CartItem.objects.all()

    if not cart_items:
        return redirect("cart")

    total_price = sum(item.total_price() for item in cart_items)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart_items:
                OrderItem.objects.create(
                    order=order, product=item.product, quantity=item.quantity
                )
            cart_items.delete()

            return redirect("thank_you")
    else:
        form = OrderForm()

    return render(
        request,
        "jewelry/checkout.html",
        {"form": form, "cart_items": cart_items, "total_price": total_price},
    )


def thank_you(request):
    return render(request, "jewelry/thank_you.html")


def about(request):
    return render(request, "jewelry/about.html")


def contacts(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "✅ Your message has been successfully sent!")
            return redirect("contacts")
    else:
        form = ContactForm()

    return render(request, "jewelry/contacts.html", {"form": form})


def page_not_found(request, exception):
    return render(request, "jewelry/404.html", status=404)
