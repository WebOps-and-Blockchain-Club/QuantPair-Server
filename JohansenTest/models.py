from django.db import models


# creating a model for each sector, a model is a python class whose variables define the columns of class
class Sectors(models.Model) :
    name = models.CharField(max_length=255, null=True)

    # making it so that the name of sector appears when viewed in django admin panel
    def __str__(self) :
        return self.name


class Stocks(models.Model) :
    name = models.CharField(max_length=255)
    # representing co-integrated stocks in terms of a json data with keys as
    # name : '<some stock name>'
    # stock_id : '<stock id>'
    coIntegratedStock = models.JSONField(null=True)
    # if owner of existing object gets deleted, set this field to null
    # we are using many-to-one relationship here as each stock has one sector
    # the parameter on_delete = models.SET_NULL gives some error, apparently it's an optional feature in newer django versions and thus we use CASCADE
    sector = models.ForeignKey(Sectors, on_delete=models.CASCADE)

    # in django admin, it will make the name of stock appear when viewing
    def __str__(self) :
        return self.name
