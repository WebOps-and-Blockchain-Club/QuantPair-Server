from django.db import models
from Signin_Signup.models import CustomUser

# our model is a one to many relationship, one being the user
class UserWishList_Pair(models.Model) :
    # symbols are the stock names 
    symbol1 = models.CharField(max_length=255, null=True)
    # two symbols as pair of stocks
    symbol2 = models.CharField(max_length=255, null=True)
    # user is the foreign key, defined in customuser, accessed when user is logged in
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # displaying the pair name in django admin 
    def __str__(self) :
        return (self.symbol1 + " " + self.symbol2)
