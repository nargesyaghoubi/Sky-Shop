from django.urls import path, include
from .views import listings

urlpatterns = [
    path('', listings, name='listings'),
]