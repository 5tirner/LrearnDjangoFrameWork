from django.db import models

class user(models.Model):
    Name = models.CharField(max_length=20)
    Age = models.CharField(max_length=3)
    Gender = models.CharField(max_length=8)
