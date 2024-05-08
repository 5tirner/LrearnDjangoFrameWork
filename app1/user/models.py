from django.db import models

class   TheUser(models.Model):
    Name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)