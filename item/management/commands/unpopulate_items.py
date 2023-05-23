from item.models import Offer, Item, Seller
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

def unpopulate_data():
    # Delete offers
    Offer.objects.all().delete()

    # Delete items
    Item.objects.all().delete()

    # Delete sellers
    Seller.objects.all().delete()

    # Delete users
    User.objects.all().delete()

    print("Data unpopulation complete.")

# Call the unpopulate_data() function to remove the data from the models



class Command(BaseCommand):
    def handle(self, *args, **options):
        unpopulate_data()
