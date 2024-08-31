from rest_framework import serializers
from .models import UserWishList_Pair

class UserWishList_PairSerializer(serializers.HyperlinkedModelSerializer) :

    class Meta : 
        model = UserWishList_Pair

        fields = '__all__'