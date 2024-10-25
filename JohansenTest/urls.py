from django.urls import path
# getting access to the views in this directory
from . import views2, views, ml_model

urlpatterns = [
    # path('<page url>', callback function)
    # other random functions and urls from first iteration, rendering html 
    path('render/', views2.JohansenTest),
    path('showSector/', views.viewSector),
    path('showStocks_Sector/', views.viewStock_Sector),
    path('showStock/', views.viewStock),

    # DONT UNCOMMENT UNLESS YOU WANT TO FILL STOCKS
    # path('populate/Sector', views.fillSector),
    # path('populate/Stock', views.fillStocks),
    # path('populate/someStock', views.fillSomeStock),
    
    path('showMLResponse/', ml_model.showPredictedOutput),
]