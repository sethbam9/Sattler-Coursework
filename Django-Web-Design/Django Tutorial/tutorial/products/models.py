from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20)
    # blank True means its not required
    # null True means 'None' is a valid DB entry
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    seller = models.TextField()
    featured = models.BooleanField()