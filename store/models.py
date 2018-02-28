from django.db import models

class Items(models.Model):
    item_text = models.CharField(max_length=200)
