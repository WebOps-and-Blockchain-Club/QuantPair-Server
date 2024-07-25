from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    # gaining access to django admin panel
    path(r'admin/', admin.site.urls),
    # adding the path of our JohansenTest to the server urls
    path(r'JohansenTest-api/', include('JohansenTest.urls')),
    # adding the path of our Signin_Sugnup to the server urls
    path(r'Users-api/', include('Signin_Signup.urls')),
]
