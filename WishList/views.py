from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import UserWishList_Pair
from .serializers import UserWishList_PairSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserWishlist(request) :

    if request.method == 'GET' :
        id = request.user.id
        queryset = UserWishList_Pair.objects.filter(user__pk=id)
        return Response(queryset.values(), status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])    
def createWishList(request) :

    if request.method == 'POST' :
        fields = request.data
        fields['user'] = str(request.user.pk)
        serializer = UserWishList_PairSerializer(data=fields)

        if(serializer.is_valid()) :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deleteWishList(request) : 

    if request.method == 'POST' :
        fields = request.data
        fields['user'] = str(request.user.pk)

        remove = None
        remove = UserWishList_Pair.objects.filter(symbol1=fields['symbol1'], symbol2=fields['symbol2'], user__id=fields['user'])
        if remove :
            remove.delete()
            return Response({'message' : 'Successfully deleted entry'}, status=status.HTTP_200_OK)
        
        return Response({'message' : 'Invalid details'}, status=status.HTTP_400_BAD_REQUEST)



