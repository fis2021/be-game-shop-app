from django.db import models

# Create your models here.


class Game(models.Model):
    key = models.CharField(blank=False, max_length=64)
    seller = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='products')
    owners = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='owned_games')

    description = models.CharField(blank=True, max_length=512)


class Category(models.Model):
    name = models.CharField(blank=False, max_length=64)
    games = models.ForeignKey('games.Game', on_delete=models.CASCADE, related_name='categories')
