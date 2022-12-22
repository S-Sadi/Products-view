from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="products_images")
    discription = models.TextField()