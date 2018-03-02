from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
