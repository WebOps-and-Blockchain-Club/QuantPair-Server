from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from . import views, views2

urlpatterns = [
    # gaining access to all registered router urls at endpoint <localhost>:<port>/User-api/<>
    path('login', views.user_login, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.user_logout, name='logout'),
    path('reset', views.user_forgot_password, name = 'reset'),
    path('user', views.getUserDetails, name='user'),
    # when we access this url path, we are redirected to the page 
    path('', views2.home, name="home"),
    path('signin', views2.signin, name="signin"),
    path('signup', views2.signup, name="signup"),
    path('signout', views2.signout, name="signout"),
    # path('activate/<uidb64>/<token>', views.activate, name="activate"),
]