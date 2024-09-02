from rest_framework import serializers
from .models import UserWishList_Pair

class UserWishList_PairSerializer(serializers.ModelSerializer) :
    # we need all fields in our serializer to take
    class Meta : 
        # referencing the model for wishlist in metadata
        model = UserWishList_Pair
        # all fields included
        fields = '__all__'
    
    # to create a new wishlist item
    def create(self, validated_data) : 
        # getting data from user and assigning into variables for better reading
        symbol1 = validated_data['symbol1']
        symbol2 = validated_data['symbol2']
        # here user is primary key of user, which is the reference to the user
        user = validated_data['user']
        # creating the wishlist item
        wishlist_item = UserWishList_Pair(symbol1=symbol1,
                                           symbol2=symbol2, 
                                           user=user)
        # savin it and returning
        wishlist_item.save()
        return wishlist_item
