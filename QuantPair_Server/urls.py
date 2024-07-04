from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    # adding the path of our JohansenTest to the server urls
    path(r'', include('JohansenTest.urls')),
    # addint the path of our Signin_Sugnup to the server urls
    path(r'', include('Signin_Signup.urls')),
]
