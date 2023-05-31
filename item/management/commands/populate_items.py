from django.core.management.base import BaseCommand
import random
from faker import Faker
import requests
from django.contrib.auth.models import User
from django.core.files import File
from io import BytesIO
from person.models import Person
from item.models import Seller, Item, ItemImage, Offer


def fetch_image_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split('/')[-1]
        image = File(BytesIO(response.content), name=file_name)
        return image
    return None


def populate_data():
    fake = Faker()

    # Create 4 persons
    persons = []
    for _ in range(4):
        # Create a user
        username = fake.user_name()
        password = fake.password()
        email = fake.email()
        user = User.objects.create_user(
            username=username, password=password, email=email)

        # Create a person
        bio = fake.text(max_nb_chars=200)
        image_url = f'https://picsum.photos/200/300?random={_+1}'
        image = fetch_image_from_url(image_url)
        if image:
            person = Person.objects.create(user=user, bio=bio, image=image)
            persons.append(person)

    # Create 20 items
    items = []
    categories = [fake.word() for _ in range(5)]
    for _ in range(20):
        # Create a seller
        seller_user = random.choice(persons).user
        seller, created = Seller.objects.get_or_create(user=seller_user)

        # Create an item
        name = f'{fake.word()} {fake.word()}'
        status = 'Available'
        condition = random.choice(['New', 'Used'])
        description = fake.text()
        category = random.choice(categories)
        price = random.randint(10, 100)
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

        # Create item images
        num_images = random.randint(1, 5)
        for _ in range(num_images):
            image_url = f'https://picsum.photos/200/300?random={_+10}'
            image = fetch_image_from_url(image_url)
            if image:
                item_image = ItemImage.objects.create(image=image, item=item)

        # Create offers for the item
        num_offers = random.randint(0, 3)
        for _ in range(num_offers):
            status = 'pending'
            amount = random.randint(10, 50)

            # TODO: Make sure buyer is not seller
            buyer = random.choice(persons).user
            offer = Offer.objects.create(
                status=status, amount=amount, item=item, buyer=buyer)


class Command(BaseCommand):
    def handle(self, *args, **options):
        populate_data()
