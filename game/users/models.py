from django.db import models

class   userInformations(models.Model):
    player = models.CharField(max_length=20)
    team = models.CharField(max_length=20)