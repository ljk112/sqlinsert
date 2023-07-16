
from django.db import models

class Clothes(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='clothes_images/')