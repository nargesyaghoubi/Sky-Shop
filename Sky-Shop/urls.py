
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Narges_log/', admin.site.urls),
    path('', include('main.urls')),
    path('listings/', include('listings.urls')),
    path('profile/', include('users.urls')),
]
