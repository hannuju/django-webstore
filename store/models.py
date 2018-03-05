#from django.urls import reverse
from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/store/item/%i/" % self.id
        #return reverse('item.views.details', args=[str(self.id)])
        #return reverse('store/item/detail', kwargs={'pk': self.pk})
