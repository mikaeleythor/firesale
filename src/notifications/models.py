from django.db import models
from django.contrib.auth.models import User


class Inbox(models.Model):
    # NOTE: incs/decs on unread implemented in service and interface classes
    unread = models.PositiveIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}-inbox'


class Notification(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    inbox = models.ForeignKey(Inbox, on_delete=models.CASCADE)
    # NOTE: specifies the name of a url pattern as seen in urls.py
    next_path = models.CharField(
        max_length=50, blank=True, default="notification-list")

    def __str__(self):
        return f'{self.title}-{self.date}'
