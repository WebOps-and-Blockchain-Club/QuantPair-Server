from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer

# creating a viewset to allow the model data to be displayed

class UserViewSet(viewsets.ModelViewSet) :
    # defining the queryset over which we are taking fields
    queryset = User.objects.all()
    # allowing this viewset the access to the metadata we created in serializer
    serializer_class = UserSerializer
