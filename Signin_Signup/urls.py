from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from . import views, views2

# using routers from rest framework for easy handling of viewsets
router = routers.DefaultRouter()
# registering our user api endpoint at <localhost>:<port>/User-api/user-api/users
router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    # gaining access to all registered router urls at endpoint <localhost>:<port>/User-api/user-api/
    path('', include(router.urls)),
    # when we access this url path, we are redirected to the page 
    path('', views2.home, name="home"),
    path('signin', views2.signin, name="signin"),
    path('signup', views2.signup, name="signup"),
    path('signout', views2.signout, name="signout"),
    # path('activate/<uidb64>/<token>', views.activate, name="activate"),
]