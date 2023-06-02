from django.db.models import F
from notifications.models import Notification


class NotificationService():

    model = Notification

    def read(self, id) -> None:
        """The exclusive interface for reading notifications"""
        instance = self.model.objects.get(id=id)
        if not instance:
            raise self.model.DoesNotExist()
        else:
            # NOTE: Idempotency
            if instance.read is False:
                instance.read = True
                instance.save()
                related = instance.inbox
                # NOTE: Decrement counter
                related.unread = F('unread') - 1
                related.save()
