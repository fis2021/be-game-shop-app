from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Default user for beGameShopApp."""

    name = models.CharField(blank=True, max_length=256)
    email = models.EmailField(blank=True, max_length=256)

    class UserTypes(models.IntegerChoices):
        CUSTOMER = 0, 'customer'
        SELLER = 1, 'seller'

    user_type = models.SmallIntegerField(choices=UserTypes.choices, default=UserTypes.CUSTOMER)

    def __str__(self):
        return self.username

    @property
    def is_customer(self):
        return self.user_type == self.UserTypes.CUSTOMER

    @property
    def is_seller(self):
        return self.user_type == self.UserTypes.SELLER
