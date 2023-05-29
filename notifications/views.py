from django.views.generic import ListView
from notifications.models import Notification


class NotificationListView(ListView):
    model = Notification
    template_name = 'notifications/notification_list.html'

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user.id)
