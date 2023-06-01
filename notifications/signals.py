from django.contrib.auth.signals import user_logged_in
from notifications.interfaces import NotificationInterface
from person.models import Person


def notify_new_user(sender, user, request, **kwargs):
    if not Person.objects.filter(user=user.id).exists():
        NotificationInterface().user_created(user)


user_logged_in.connect(notify_new_user)
