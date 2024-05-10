from django.db import models

class   userGameInfos(models.Model):
    Name = models.CharField(max_length=20)
    Age  = models.IntegerField()
    Nickname = models.CharField(max_length=15)
    level = models.IntegerField(default=0)
    GameNumbers = models.IntegerField(default=0)
    GameWin = models.IntegerField(default=0)
    GameLose = models.IntegerField(default=0)
    FriendNumbers = models.IntegerField(default=0)
    BlockList = models.IntegerField(default=0)