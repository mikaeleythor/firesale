from django.db.models import F
from notifications.models import Notification, Inbox


class NotificationInterface():
    """This is an interface for other apps in this project"""

    model = Notification
    manager = Inbox

    def offer_accepted(self, offer):
        seller = offer.item.seller.user
        seller_msg_title = 'You\'ve just accepted an offer'
        seller_msg_body = f'{seller_msg_title} of {offer.amount} for {offer.item}'
        self.__notify(seller, seller_msg_title, seller_msg_body)

        buyer = offer.buyer
        buyer_msg_title = f'{seller.username} accepted your offer'
        buyer_msg_body = f'{buyer_msg_title} of {offer.amount} for {offer.item}'
        self.__notify(buyer, buyer_msg_title, buyer_msg_body)

    def __notify(self, user, title, body):
        inbox, created = self.manager.objects.get_or_create(user=user)
        self.model.objects.create(
            title=title,
            message=body,
            inbox=inbox
        )
        inbox.unread = F('unread') + 1
