from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Game(models.Model):
    key = models.CharField(blank=False, max_length=64)
    seller = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='products')
    owners = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='owned_games')

    description = models.CharField(blank=True, max_length=512)


class Category(models.Model):
    name = models.CharField(blank=False, max_length=64)
    games = models.ForeignKey('games.Game', on_delete=models.CASCADE, related_name='categories')


class Review(models.Model):
    rating = models.PositiveSmallIntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='reviews')
    game = models.ForeignKey('games.Game', on_delete=models.CASCADE, related_name='reviews')

    description = models.CharField(blank=True, max_length=64)
