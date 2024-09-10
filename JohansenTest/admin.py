from django.contrib import admin
from .models import Sectors, Stocks

# allowing django admin the access to modify these tables
admin.site.register(Sectors)
admin.site.register(Stocks)
