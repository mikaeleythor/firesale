from django.db import models
from django.contrib.auth.models import User


def item_photo_directory_path(instance, filename):
    return f'item/{instance.item.name}/{filename}'


class Seller(models.Model):
    rating = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Item(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class ItemImage(models.Model):
    image = models.ImageField(upload_to=item_photo_directory_path)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f'image-{self.id}'


class Offer(models.Model):
    status = models.CharField(max_length=255)
    amount = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.status}-{self.amount}'
