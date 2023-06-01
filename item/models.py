from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def item_photo_directory_path(instance, filename):
    return f'item/{instance.item.name}/{filename}'


def validate_offer_status(value):
    if value not in ['Accepted', 'Pending', 'Declined', 'Confirmed']:
        raise ValidationError(
            "Status must be Accepted, Pending, Declined or Confirmed")
    return value


def validate_item_status(value):
    if value not in ['Available', 'Waiting for payment', 'Sold']:
        raise ValidationError(
            "Status must be Available, Waiting for payment or Sold")
    return value


class Seller(models.Model):
    rating = models.PositiveIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Item(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255,
                              validators=[validate_item_status],
                              default='Available')
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
        return f'{self.item.name}-image-{self.id}'


class Offer(models.Model):
    status = models.CharField(max_length=255,
                              validators=[validate_offer_status],
                              default='Pending')
    amount = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.status}-{self.amount}'
