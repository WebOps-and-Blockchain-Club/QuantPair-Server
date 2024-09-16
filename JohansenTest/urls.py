from django.urls import path
# getting access to the views in this directory
from . import views2, views

urlpatterns = [
    # path('<page url>', callback function)
    # including the router urls we configured above with endpoint <localhost>:<port>/JohansenTest-api/stock-api
    # path('stock-api/', include(router.urls)),
    # other random functions and urls from first iteration, rendering html 
    path('render/', views2.JohansenTest),
    path('populate/Sector', views.fillSector),
    # path('populate/Stock', populate_db.fillStocks),
    path('populate/someStock', views.fillSomeStock),
]