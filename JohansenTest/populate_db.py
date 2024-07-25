import requests
from .models import Sectors

url = "https://financialmodelingprep.com/api/v3/stock-screener?apikey=pvDMXekTNwD8iPfQ9K8aCnLuXyvAUvYT"

list = ["Consumer Cyclical", "Energy, Technology", "Industrials", "Financial Services", "Basic Materials", "Communication Services"
    , "Consumer Defensive", "Healthcare", "Real Estate", "Utilities", "Industrial Goods", "Financial", "Services", "Conglomerates"]

# adding to the sectors database
for x in list :
    sector = Sectors.objects.create(x)
    sector.save()

