from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from item.models import Seller, Item, Offer

def populate_data():
    # Create users
    user1 = User.objects.create_user(username='user1', password='password1')
    user2 = User.objects.create_user(username='user2', password='password2')
    user3 = User.objects.create_user(username='user3', password='password3')

    # Create sellers
    seller1 = Seller.objects.create(rating=4, user=user1)
    seller2 = Seller.objects.create(rating=3, user=user2)
    seller3 = Seller.objects.create(rating=5, user=user3)

    # Create items
    item1 = Item.objects.create(name='Item 1', status='Available', condition='New',
                                description='Description for Item 1', category='Category 1',
                                price=100, seller=seller1)
    item2 = Item.objects.create(name='Item 2', status='Sold', condition='Used',
                                description='Description for Item 2', category='Category 2',
                                price=50, seller=seller2)
    item3 = Item.objects.create(name='Item 3', status='Available', condition='New',
                                description='Description for Item 3', category='Category 1',
                                price=80, seller=seller3)

    # Create offers
    offer1 = Offer.objects.create(status='Pending', amount=90, item=item1, buyer=user2)
    offer2 = Offer.objects.create(status='Accepted', amount=40, item=item2, buyer=user1)
    offer3 = Offer.objects.create(status='Rejected', amount=70, item=item3, buyer=user3)

    print("Data population complete.")

# Call the populate_data() function to populate the models with template data



class Command(BaseCommand):
    def handle(self, *args, **options):
        populate_data()