import requests
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
import json
from .models import Sectors, Stocks

from django.template import loader

# list of all possible sectors in the api
list = ["Consumer Cyclical", "Energy", "Technology", "Industrials", "Financial Services", "Basic Materials", "Communication Services"
    , "Consumer Defensive", "Healthcare", "Real Estate", "Utilities", "Industrial Goods", "Financial", "Services", "Conglomerates"]

# adding to the sectors database
def fillSector (request) :
    # iterating through the list and for each element, we create a new row with the sector name
    for x in list :
        sector = Sectors.objects.create(name=x)
        sector.save()

# adding stocks to the stocks database
def fillStocks (request) :
    apiKey = "pvDMXekTNwD8iPfQ9K8aCnLuXyvAUvYT"
    # iterating through the list of sectors
    for sector in list :
        # for each sector in the list, we make an api call to fetch all stocks in that sector
        url = "https://financialmodelingprep.com/api/v3/stock-screener?sector={sector}&apikey={apiKey}"
        # getting the response
        response = requests.get(url)
        # we check if the response is ok
        if response.status_code == 200 :
            # get the sector from sectors model in database to associate it with our stock into consideration
            query_sector = Sectors.objects.filter(name=sector)
            # getting json data
            data = response.json()
            # iterating through the json data and creating a new stock, filling the stocks row
            for obj in data :
                stock = Stocks.objects.create(name=obj.symbol, cointegrated_stock={}, sector=query_sector)
                stock.save()

def fillSomeStock(request) :
    apiKey = "pvDMXekTNwD8iPfQ9K8aCnLuXyvAUvYT"
    sector = "Financial"
    url = f"https://financialmodelingprep.com/api/v3/stock-screener?sector={sector}&apikey={apiKey} "
    print(url)
    response = requests.get(url)
    print(url + "\n")
    if response.status_code == 200 :
        query_sector = Sectors.objects.filter(name=sector)
        data = response.json()
        
        iter = 0
        for obj in data :
            iter += 1
            print(obj.symbol)
            print("\n")
            # stock = Stocks.objects.create(name = obj.symbol, cointegrated_stock = {}, sector = query_sector)
            # stock.save()
            if iter > 9 :
                break
    
    
    




