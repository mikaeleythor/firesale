from django.http import JsonResponse
from django.views.generic import ListView
from notifications.models import Notification, Inbox
from notifications.services import NotificationService


class NotificationListView(ListView):
    model = Notification
    template_name = 'notifications/notification_list.html'

    def get_queryset(self):
        inbox, created = Inbox.objects.get_or_create(user=self.request.user)
        return Notification.objects.filter(inbox=inbox.id).order_by('-date')


def read(request, id):
    if request.method == 'POST':
        NotificationService().read(id)
        return JsonResponse(status=200, data={"message": "Message read"})
    return JsonResponse(status=400, data={"message": "Unsupported method"})
