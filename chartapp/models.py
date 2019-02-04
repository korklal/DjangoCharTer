import uuid

from django.db import models


# Create your models here.

class Product(models.Model):

    slug= models.SlugField()
    id= models.CharField(max_length=120, primary_key=True)
    price: float = models.FloatField()
    name: str = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name

#
# class Selling():
#
#     def __init__(self, prodects_name):
#         self.products_name=prodects_name
#
#         self.product_store: dict = [Product]
#
#     def count_seling(self, product, selling, summe_from_selling):
#         self.product_store.append(product)
#         self.selling: int = selling
#         self.summe_from_selling: float = summe_from_selling
