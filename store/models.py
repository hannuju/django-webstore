from django.db import models
from django.urls import reverse

class Item(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('store:item-detail', args=[str(self.id)])
