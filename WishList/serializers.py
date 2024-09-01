from rest_framework import serializers
from .models import UserWishList_Pair

class UserWishList_PairSerializer(serializers.ModelSerializer) :

    class Meta : 
        model = UserWishList_Pair

        fields = '__all__'
    
    def create(self, validated_data) : 
        symbol1 = validated_data['symbol1']
        symbol2 = validated_data['symbol2']
        user = validated_data['user']
        wishlist_item = UserWishList_Pair(symbol1=symbol1,
                                           symbol2=symbol2, 
                                           user=user)
        wishlist_item.save()
        return wishlist_item
