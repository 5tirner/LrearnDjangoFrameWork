from django.db import models

class personalInfos(models.Model):
    GameName = models.CharField(max_length=255)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
