from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Sectors, Stocks
from .serializers import SectorSerializer, StockSerializer
import requests
import random


@api_view(['GET'])
@permission_classes([])
def viewSector(request) : 
    if request.method == 'GET' :
        queryset = Sectors.objects.all()

        return Response(queryset.values(), status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([])
def viewStock_Sector(request) : 
    if request.method == 'POST' :
        fields = request.data
        sector = fields['sector']
        queryset = Stocks.objects.filter(sector__name=sector)

        return Response(queryset.values(), status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([])
def viewStock(request) : 
    if request.method == 'POST' :
        fields = request.data
        symbol = fields['symbol']
        queryset = Stocks.objects.filter(name=symbol)

        return Response(queryset.values(), status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([])
def fillSomeStock(request) : 
    if request.method == 'GET' : 
        apiKey = "pvDMXekTNwD8iPfQ9K8aCnLuXyvAUvYT"
        sector = "Energy"
        url = f"https://financialmodelingprep.com/api/v3/stock-screener?sector={sector}&apikey={apiKey}"
        response = requests.get(url)

        if response.status_code == 200 :
            query_sector = Sectors.objects.get(name=sector)
            fields = response.json()
            iter = 0
            for obj in fields :
                temp = {}
                temp['name'] = obj['symbol']
                temp['coIntegratedStock'] = {"stk_1" : random.random(), "stk_2" : random.random()}
                temp['sector'] = query_sector.pk
                iter += 1
                serializer = StockSerializer(data=temp)
                if(serializer.is_valid()) :
                    serializer.save()
                    print("VALID")
                    # pass
                else :
                    # print("NOT VALID")
                    print(serializer.errors)
                if iter > 50 :
                    return Response({'message' : 'Successfully filled table'}, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
@permission_classes([])
def fillStocks(request) :
    if request.method == 'GET' : 
        apiKey = "pvDMXekTNwD8iPfQ9K8aCnLuXyvAUvYT"
        sector = "Financial Services"
        url = f"https://financialmodelingprep.com/api/v3/stock-screener?sector={sector}&apikey={apiKey}"
        response = requests.get(url)

        if response.status_code == 200 :
            query_sector = Sectors.objects.get(name=sector)
            data = response.json()
            for obj in data :
                temp = {}
                temp['name'] = obj['symbol']
                temp['coIntegratedStock'] = {}
                temp['sector'] = query_sector.pk
                iter += 1
                serializer = StockSerializer(data=temp)
                if(serializer.is_valid()) :
                    serializer.save()
                    print("VALID")
                    # pass
                else :
                    # print("NOT VALID")
                    print(serializer.errors)

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
    