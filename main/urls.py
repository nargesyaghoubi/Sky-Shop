from django.urls import path, include
from .views import index, shop, cart, checkout

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout')

]