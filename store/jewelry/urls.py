from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("products/", views.products, name="products"),
    path("category/<slug:slug>/", views.category_view, name="category"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("cart/", views.cart, name="cart"),
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path(
        "cart/remove/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"
    ),
    path(
        "cart/update/<int:product_id>/", views.update_cart_item, name="update_cart_item"
    ),
    path("cart/clear/", views.clear_cart, name="clear_cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("thank-you/", views.thank_you, name="thank_you"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
