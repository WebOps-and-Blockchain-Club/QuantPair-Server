from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.exceptions import ObjectDoesNotExist
from .serializers import CustomUserSerializer
from .models import CustomUser

# defining custom api views using api_view as ViewSets dont provide flexibility with handling of registering users 
# function based api views using the django decorator api_view which gives metadata indicating this method is api-view
@api_view(['POST'])
def register_user(request) : 
    # if POST request is made
    if request.method == "POST" :
        # use the serializer defined and check if all fields are valid
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid() :
            # save if valid to database
            serializer.save()
            # return some message that successfully saved busing http status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if not valid, send error message
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([])
def user_login(request) :
    if request.method == "POST" :
        # getting the username and password fields from the data sent
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def user_logout(request) : 
    if request.method == "POST" :
        try:
            # deleting the user token to log the user out
            logout(request)
            request.user.auth_token.delete()
            # success message 
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            # error handling
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


