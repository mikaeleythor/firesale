from django.contrib import admin
from item.models import Item, ItemImage, Seller, Offer, SellerRating

admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(Seller)
admin.site.register(SellerRating)
admin.site.register(Offer)
