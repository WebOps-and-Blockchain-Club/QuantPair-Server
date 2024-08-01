from django.db import models
from django.contrib.auth.models import AbstractUser

# creating a custom user model in django for handling api requests
class CustomUser(AbstractUser) : 
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self) :
        return self.fname
