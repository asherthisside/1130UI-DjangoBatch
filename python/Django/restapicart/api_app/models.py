from django.db import models

# Create your models here.
class Shoppingcart(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.product_name