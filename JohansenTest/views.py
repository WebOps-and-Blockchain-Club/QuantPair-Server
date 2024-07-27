from rest_framework import viewsets
from .models import Sectors, Stocks
from .serializers import SectorSerializer, StockSerializer

# creating a viewset to allow the model data to be displayed

class SectorViewSet(viewsets.ModelViewSet) :
    # defining the queryset over which we are taking fields
    queryset = Sectors.objects.all()
    # allowing this viewset the access to the metadata we created in serializer
    serializer_class = SectorSerializer

class StockViewSet(viewsets.ModelViewSet) :
    # defining the queryset over which we are taking fields
    queryset = Stocks.objects.all()
    # allowing this viewset the access to the metadata we created in serializer
    serializer_class = StockSerializer

