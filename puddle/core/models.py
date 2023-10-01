from django.db import models

# Create your models here.

class Item(models.Model):
    category = models.CharField(max_length=100)