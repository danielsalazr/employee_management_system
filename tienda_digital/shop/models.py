from statistics import mode
from tracemalloc import stop
from django.db import models

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
# Create your models here.
class Productos(models.Model):
    sku = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to= upload_to, default="")