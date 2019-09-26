import uuid

from django.db import models


# Create your models here.

class Product(models.Model):
    slug = models.SlugField()
    id = models.CharField(max_length=120, primary_key=True)
    price: float = models.FloatField()
    name: str = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name


from django.db import models


class Contact(models.Model):
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )

    email = models.EmailField()

    def __str__(self):
        return '{}{}'.format(
            self.first_name,
            self.last_name,
        )
