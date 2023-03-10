from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.product, name='product_detail'),
    path("search/", views.search, name='search'), 
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('cart/delete/<int:product_id>', views.cart_delete, name='cart_delete'),
    path('cart/buying/', views.buying, name='buying'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>', views.wishlist_add, name='wishlist_add'),
    path('wishlist/delete/<int:product_id>', views.wishlist_delete,  name='wishlist_delete'),
    path('account/create/', views.signUp, name='signup'),
    path('account/login/', views.logIn, name='login'),
    path('account/logout/', views.signOut, name='signout'),
]