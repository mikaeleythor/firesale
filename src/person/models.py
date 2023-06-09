from django.db import models
from django.contrib.auth.models import User


def person_photo_directory_path(instance, filename):
    return f'person/{instance.user.username}/{filename}'


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to=person_photo_directory_path, default='person/anonymous.png'
    )

    def __str__(self):
        return f'{self.id}-{self.user.username}'
