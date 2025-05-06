from django.urls import path, include
from .views import signup, signin

urlpatterns = [
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
]