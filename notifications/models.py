from django.db import models
from django.contrib.auth.models import User


class Inbox(models.Model):
    # WARNING: Increments/Decrements on unread should be implemented in service
    unread = models.PositiveIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Notification(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    inbox = models.ForeignKey(Inbox, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}-{self.date}'
