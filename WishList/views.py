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


