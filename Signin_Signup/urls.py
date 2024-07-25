from django.contrib import admin
from django.urls import path, include
from . import views2

urlpatterns = [
    # when we access this url path, we are redirected to the page 
    path('', views2.home, name="home"),
    path('signin', views2.signin, name="signin"),
    path('signup', views2.signup, name="signup"),
    path('signout', views2.signout, name="signout"),
    # path('activate/<uidb64>/<token>', views.activate, name="activate"),
]