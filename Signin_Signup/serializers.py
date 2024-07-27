from rest_framework import serializers
from django.contrib.auth.models import User


# creating a serializer to enable data parsing between json and viewable format
# using HyperlinkedModelSerializer gives an error as User model in django.contrib.auth.models does not have a view with name user-details, which is essential for HyperlinkedModelSerializer
class UserSerializer(serializers.ModelSerializer) :
    # specifying metadata like models and fields of our models to display
    class Meta :
        # defining the model in consideration
        model = User
        # specifying which fields we want to take
        fields = '__all__'
