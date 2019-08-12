from django.db import models


class Phone(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
