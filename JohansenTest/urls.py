from django.urls import path, include
# getting access to the views in this directory
from . import views2, populate_db, views
# importing rest framework to use routers
from rest_framework import routers

# using routers from rest framework for easy handling of viewsets
router = routers.DefaultRouter()
# registering the endpoint to <localhost>:<port>/JohansenTest-api/stock-api/sector/
router.register('sector', views.SectorViewSet)
# registering the endpoint for all stocks with cointegrated stocks in the endpoint <localhost>:<port>/JohansenTest-api/stock-api/stock/
router.register('stock', views.StockViewSet)

urlpatterns = [
    # path('<page url>', callback function)
    # including the router urls we configured above with endpoint <localhost>:<port>/JohansenTest-api/stock-api
    path('stock-api/', include(router.urls)),
    # other random functions and urls from first iteration, rendering html 
    path('render/', views2.JohansenTest),
    path('populate/Sector', populate_db.fillSector),
    path('populate/Stock', populate_db.fillStocks),
]