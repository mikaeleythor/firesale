from django.contrib import admin
from notifications.models import Notification, Inbox

admin.site.register(Notification)
admin.site.register(Inbox)
