from django.db import models

# Create your models here.
class register(models.Model):
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
