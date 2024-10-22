import requests
import random
import json
from .models import Sectors, Stocks

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
    # sector = "Technology"
    apiKey = "pvDMXekTNwD8iPfQ9K8aCnLuXyvAUvYT"
    # iterating through the list of sectors
    for sector in list :
        # for each sector in the list, we make an api call to fetch all stocks in that sector
        url = "https://financialmodelingprep.com/api/v3/stock-screener?sector=", sector,"&apikey=", apiKey
        # getting the response
        response = requests.get(url)
        # we check if the response is ok
        count = 0
        if response.status_code == 200 :
            # get the sector from sectors model in database to associate it with our stock into consideration
            query_sector = Sectors.objects.filter(name=sector)
            # getting json data
            data = response.json()

            # iterating through the json data and creating a new stock, filling the stocks row
            for obj in data :
                stock = Stocks.objects.create(name=obj.symbol, cointegrated_stock={"stk_1" : random.random(), "stk_2" : random.random()}, sector=query_sector)
                stock.save()
                count += 1
                if count > 50 :
                    break




