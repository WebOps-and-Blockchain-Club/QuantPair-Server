from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import UserWishList_Pair
from .serializers import UserWishList_PairSerializer

# endpoint view for getting the wishlist of that user
@api_view(['GET'])
# can have wishlist iff authenticated
@permission_classes([IsAuthenticated])
def getUserWishlist(request) :
    # as it is a get request, for extra safety
    if request.method == 'GET' :
        # gaining the user id, which is the primary key for user
        id = request.user.id
        # making query to get all of that particular user's wishlist
        queryset = UserWishList_Pair.objects.filter(user__pk=id)
        # returning the query
        return Response(queryset.values(), status=status.HTTP_200_OK)

# api endpoint to create a new wishlist item
@api_view(['POST'])
# can have wishlist iff authenticated
@permission_classes([IsAuthenticated])    
def createWishList(request) :
    # post method check
    if request.method == 'POST' :
        # getting the POST data
        fields = request.data
        # adding the user to the fields, to ease the process of foreign key addition
        fields['user'] = str(request.user.pk)
        # passing data to serializer to create the object
        serializer = UserWishList_PairSerializer(data=fields)
        # if all fields are valid, then save
        if(serializer.is_valid()) :
            serializer.save()
            # return the data saved and approprialte success HTTP status
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        # in case invalid, BAD request error handling
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Deleting a particular wishlist item
@api_view(['POST'])
# only authenticated users can make this query
@permission_classes([IsAuthenticated])
def deleteWishList(request) : 
    # condition check
    if request.method == 'POST' :
        # getting the data
        fields = request.data
        fields['user'] = str(request.user.pk)
        # initializing the remove to none for error handling
        remove = None
        # if present, get the item
        remove = UserWishList_Pair.objects.filter(symbol1=fields['symbol1'], symbol2=fields['symbol2'], user__id=fields['user'])
        # if remove is not None, delete
        if remove :
            remove.delete()
            # success message
            return Response({'message' : 'Successfully deleted entry'}, status=status.HTTP_200_OK)
        # if item not present, bad request
        return Response({'message' : 'Invalid details'}, status=status.HTTP_400_BAD_REQUEST)



