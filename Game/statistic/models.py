from django.db import models

class infos(models.Model):
    userName = models.CharField(max_length = 30)
    clan = models.CharField(max_length = 30)
    level = models.IntegerField(default = 0)
    games = models.IntegerField(default = 0)
    wins = models.IntegerField(default = 0)
    loses = models.IntegerField(default = 0)
