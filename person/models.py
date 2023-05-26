from django.db import models
from django.contrib.auth.models import User


def person_photo_directory_path(instance, filename):
    return f'person/{instance.user.username}/{filename}'


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    # TODO This causes an error, this needs fixing
    # image = models.ImageField(upload_to=person_photo_directory_path)
