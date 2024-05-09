from django.db import models

class table1(models.Model):
    TheString = models.CharField(max_length = 255)
    Describ = models.CharField(max_length = 255)
