from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


def unpopulate_data():
    """
    Deletes all users which are not superusers
    this cascades to delete all Items, Offers, Inboxes which do not belong
    to superusers
    """
    User.objects.filter(is_staff=False).delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        unpopulate_data()
