from django.db import models
from Signin_Signup.models import CustomUser

class UserWishList_Pair(models.Model) :
    symbol1 = models.CharField(max_length=255, null=True)
    symbol2 = models.CharField(max_length=255, null=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self) :
        return (self.symbol1 + " " + self.symbol2)
