from rest_framework import serializers
from .models import CustomUser


# creating a serializer to enable data parsing between json and viewable format
# using HyperlinkedModelSerializer gives an error as User model in django.contrib.auth.models does not have a view with name user-details, which is essential for HyperlinkedModelSerializer
class CustomUserSerializer(serializers.ModelSerializer) :
    # specifying metadata like models and fields of our models to display
    class Meta :
        # defining the model in consideration
        model = CustomUser
        # specifying which fields we want to take
        fields = '__all__'

    def create(self, validated_data) :
        user = CustomUser(
            fname = validated_data['fname'],
            lname = validated_data['lname'],
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user