from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # using the django auth app to configure signin-signup routes and gaining access to django administration 
    path("admin/", admin.site.urls),
    # when we access this url path, we are redirected to the page? 
    # the auth application contains default views and url patterns for signin page
    # url patterns : 
        # accounts/login/ [name='login']
        # accounts/logout/ [name='logout']
        # accounts/password_change/ [name='password_change']
        # accounts/password_change/done/ [name='password_change_done']
        # accounts/password_reset/ [name='password_reset']
        # accounts/password_reset/done/ [name='password_reset_done']
        # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
        # accounts/reset/done/ [name='password_reset_complete']
    path('', views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
]