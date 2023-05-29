from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}-{self.date}'
