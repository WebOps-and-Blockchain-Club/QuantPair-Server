from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Sectors, Stocks
from .serializers import SectorSerializer, StockSerializer
import requests


@api_view(['GET'])
@permission_classes([])
def viewSector(request) : 
    if request.method == 'GET' :
        queryset = Sectors.objects.all()

        return Response(queryset.values(), status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([])
def viewStock_Sector(request) : 
    if request.method == 'GET' :
        fields = request.data
        sector = fields['sector']
        queryset = Stocks.objects.filter(sector=sector)

        return Response(queryset.values(), status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([])
def fillSomeStock(request) : 
    if request.method == 'GET' : 
        apiKey = "pvDMXekTNwD8iPfQ9K8aCnLuXyvAUvYT"
        sector = "Financial Services"
        url = f"https://financialmodelingprep.com/api/v3/stock-screener?sector={sector}&apikey={apiKey}"
        response = requests.get(url)

        if response.status_code == 200 :
            query_sector = Sectors.objects.filter(name=sector)
            data = response.json()
            iter = 0
            for obj in data :
                iter += 1
                # stock = Stocks.objects.create(name = obj.symbol, cointegrated_stock = {}, sector = query_sector)
                # stock.save()
                if iter > 9 :
                    break

            return Response({'message' : 'Successfully filled table'}, status=status.HTTP_200_OK)
        
@api_view(['GET'])
@permission_classes([])
def fillStocks(request) :
    if request.method == 'GET' : 
        apiKey = "pvDMXekTNwD8iPfQ9K8aCnLuXyvAUvYT"
        sector = "Financial Services"
        url = f"https://financialmodelingprep.com/api/v3/stock-screener?sector={sector}&apikey={apiKey}"
        response = requests.get(url)

        if response.status_code == 200 :
            query_sector = Sectors.objects.filter(name=sector)
            data = response.json()
            for obj in data :
                # stock = Stocks.objects.create(name = obj.symbol, cointegrated_stock = {}, sector = query_sector)
                # stock.save()
                continue

            return Response({'message' : 'Successfully filled table'}, status=status.HTTP_200_OK)

list = ["Consumer Cyclical", "Energy", "Technology", "Industrials", "Financial Services", "Basic Materials", "Communication Services"
    , "Consumer Defensive", "Healthcare", "Real Estate", "Utilities", "Industrial Goods", "Financial", "Services", "Conglomerates"]

@api_view(['GET'])
@permission_classes([])
# adding to the sectors database
def fillSector (request) :
    # iterating through the list and for each element, we create a new row with the sector name
    for x in list :
        sector = Sectors.objects.create(name=x)
        sector.save()

    return Response({'message' : 'Successfully filled table'}, status=status.HTTP_200_OK)
    