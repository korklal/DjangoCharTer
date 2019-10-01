from django.db import models


class Product(models.Model):
    slug = models.SlugField()
    id = models.CharField(max_length=120, primary_key=True)
    price: float = models.FloatField()
    name: str = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )

    email = models.EmailField()

    id = models.IntegerField(auto_created=True, primary_key=True)

    def __str__(self):
        return '{}{}'.format(
            self.first_name,
            self.last_name,
        )

    @property
    def about(self):
        return -1


class ContactInteraction(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=255)
    url_field = models.URLField(max_length=255)

    @property
    def contact(self):
        return Contact.objects.get(first_name="qqq")

    @property
    def contacts(self):
        return models.ForeignKey(
            Contact,
            on_delete=models.CASCADE,
            related_name='last_name'
        )

