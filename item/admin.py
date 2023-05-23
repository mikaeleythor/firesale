from django.contrib import admin
from item.models import Item, ItemImage, Seller, Offer

# Register your models here.
admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(Seller)
admin.site.register(Offer)
