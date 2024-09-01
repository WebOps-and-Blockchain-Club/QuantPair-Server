from django.urls import path
from . import views

urlpatterns = [
    path('getWishList', views.getUserWishlist, name='getWishList'),
    path('createWishList', views.createWishList, name='createWishList'),
    path('deleteWishList', views.deleteWishList, name='deleteWishList'),
]