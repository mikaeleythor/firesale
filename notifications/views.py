from django.views.generic import ListView
from notifications.models import Notification, Inbox


class NotificationListView(ListView):
    model = Notification
    template_name = 'notifications/notification_list.html'

    def get_queryset(self):
        inbox, created = Inbox.objects.get_or_create(user=self.request.user)
        return Notification.objects.filter(inbox=inbox.id)
