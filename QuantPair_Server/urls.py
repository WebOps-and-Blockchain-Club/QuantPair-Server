from django.contrib import admin
from django.urls import path, include
# adding the path of our JohansenTest to the server urls
urlpatterns = [
    path(r'', include('JohansenTest.urls'))
]
