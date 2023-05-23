from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Seller(models.Model):
    rating = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)


class ItemImage(models.Model):
    image = models.CharField(max_length=9999)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class Offer(models.Model):
    status = models.CharField(max_length=255)
    amount = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer = models.OneToOneField(User, on_delete=models.CASCADE)

