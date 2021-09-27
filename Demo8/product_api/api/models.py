from django.db import models
from django.db.models.fields import TextField

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    category = models.DecimalField(max_digits=4, decimal_places=2)
    descriptions = models.TextField()
    stars = models.IntegerField()

    def __str__(self):
        return self.name
        
