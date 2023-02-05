from django.urls import path
from .views import ProductListView, ProductDetailView, wishlist_view, WishlistListView, ShoppingCartView, cart_view

app_name = 'products'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='all'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('wishlist/<int:id>/', wishlist_view, name='wishlist'),
    path('wishlist/', WishlistListView.as_view(), name='wishlist_list'),
    path('shopping_cart/', ShoppingCartView.as_view(), name='shopping_cart'),
    path('add_cart/<int:id>/', cart_view, name='cart'),
    
]