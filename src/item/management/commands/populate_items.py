from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.files import File
from item.models import Seller, Item, ItemImage, Offer
from person.models import Person
from faker import Faker
from io import BytesIO
import requests
import random


def fetch_image_from_url(url):
    """Returns File object containing an image fetched from given url"""
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split('/')[-1]
        image = File(BytesIO(response.content), name=file_name)
        return image
    return None


def populate_data():
    """
    Creates the following related objects from randomly generated data
    - 4 User instances
    - 4 Person instances
    - 20 Item instances
    - 1 to 20 Seller instances
    - 20 to 100 ItemImage instances
    - 0 to 60 Offer instances
    """
    fake = Faker()

    # NOTE: Create 4 Person instances
    persons = []
    for _ in range(4):
        # NOTE: Create a User instance
        username = fake.user_name()
        password = fake.password()
        email = fake.email()
        user = User.objects.create_user(
            username=username, password=password, email=email)

        # NOTE: Create a Person instance
        bio = fake.text(max_nb_chars=200)
        image_url = f'https://picsum.photos/200/300?random={_+1}'
        image = fetch_image_from_url(image_url)
        if image:
            person = Person.objects.create(user=user, bio=bio, image=image)
            persons.append(person)

    # NOTE: Create 20 Item instances
    items = []
    categories = [fake.word() for _ in range(5)]
    for _ in range(20):

        # NOTE: Create a Seller instance
        seller_user = random.choice(persons).user
        seller, created = Seller.objects.get_or_create(user=seller_user)

        # NOTE: Create the Item instance
        name = f'{fake.word()} {fake.word()}'
        name = name[0].upper() + name[1:]
        status = 'Available'
        condition = random.choice(['New', 'Used'])
        description = fake.text()
        category = random.choice(categories)
        price = random.randint(1000, 100000)
        item = Item.objects.create(
            name=name,
            status=status,
            condition=condition,
            description=description,
            category=category,
            price=price,
            seller=seller
        )
        items.append(item)

        # NOTE: Create ItemImage instances
        num_images = random.randint(1, 5)
        for _ in range(num_images):
            image_url = f'https://picsum.photos/200/300?random={_+10}'
            image = fetch_image_from_url(image_url)
            if image:
                ItemImage.objects.create(image=image, item=item)

        # NOTE: Create Offer instance for the Item
        num_offers = random.randint(0, 3)
        for _ in range(num_offers):
            status = 'pending'
            amount = random.randint(10, 50)

            # NOTE: Set initial value of buyer to seller
            buyer = item.seller.user

            # NOTE: Make sure buyer is not seller
            while buyer.id != item.seller.user.id:
                buyer = random.choice(persons).user

            Offer.objects.create(
                status=status, amount=amount, item=item, buyer=buyer)


class Command(BaseCommand):
    def handle(self, *args, **options):
        populate_data()
