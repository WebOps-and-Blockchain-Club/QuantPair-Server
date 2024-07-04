from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #hi
    # using the django auth app to configure signin-signup routes and gaining access to django administration 
    path("admin/", admin.site.urls),
    # when we access this url path, we are redirected to the page 
    path('', views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
    # path('activate/<uidb64>/<token>', views.activate, name="activate"),
]