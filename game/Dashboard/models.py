from django.db import models

class usrInfo(models.Model):
    Username = models.CharField(max_length = 30)
    Clan = models.CharField(max_length = 30)
    Level = models.IntegerField(default = 0)
    Play = models.IntegerField(default = 0)
    Wins = models.IntegerField(default = 0)
    Loses = models.IntegerField(default = 0)
    Friends = models.IntegerField(default = 0)

class points(models.Model):
    pointsAmounts = models.IntegerField(default = 0)