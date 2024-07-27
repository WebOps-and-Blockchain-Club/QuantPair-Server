from rest_framework import serializers
from .models import Stocks, Sectors


# creating a serializer to enable data parsing between json and viewable format
class SectorSerializer(serializers.HyperlinkedModelSerializer) :
    # specifying metadata like models and fields of our models to display
    class Meta :
        # defining the model in consideration
        model = Sectors
        # specifying which fields we want to take
        fields = '__all__'

class StockSerializer(serializers.HyperlinkedModelSerializer) :
    # specifying metadata like models and fields of our models to display
    class Meta : 
        # defining the model in consideration
        model = Stocks
        # specifying the fields we want in json data, we can take all or some fields by 
        # manually keeping them as a tuple ('<field name>', '<field name>' ...)
        fields = '__all__'