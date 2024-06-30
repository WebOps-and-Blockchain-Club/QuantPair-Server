from django.urls import path
# getting access to the views in this directort
from . import views

urlpatterns = [
    # firing the JohansenTest function when we access this webpage
    # path('<page url', callback function)
    path('JohansenTest/', views.JohansenTest)
]