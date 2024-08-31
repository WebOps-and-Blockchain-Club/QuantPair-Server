from django.urls import path
from . import views

urlpatterns = [
    path('getWishList', views.getUserWishlist, name='getWishList'),
]