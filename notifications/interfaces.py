from django.db.models import F
from notifications.models import Notification, Inbox


class NotificationInterface():
    """
    This is an interface for other apps in this project

    Each accessible method handles a single notification operation

    Other logic should be handled in other domains
    """

    model = Notification
    manager = Inbox

    def user_created(self, user):
        # WARNING: This should be provided from views instead of hardcoded here
        next_path_name = 'create-person'
        msg_title = 'Finish setting up your profile'
        msg_body = 'Welcome to FireSale! Click here to finish setting up your profile'
        self.__notify(user, msg_title, msg_body, next_path_name)

    def payment_received(self, payer, recipient, amount, item):
        msg_title = f'Payment from {payer.username}'
        msg_body = f'Payment of {amount}kr for {item} from {payer.username} has been received'
        self.__notify(recipient, msg_title, msg_body)

    def offer_accepted(self, offer):
        # WARNING: This should be provided from views instead of hardcoded here
        next_path_name = 'checkout'
        seller = offer.item.seller.user
        buyer = offer.buyer
        buyer_msg_title = f'{seller.username} accepted your offer'
        buyer_msg_body = f'{buyer_msg_title} of {offer.amount} on {offer.item}'
        self.__notify(buyer, buyer_msg_title, buyer_msg_body, next_path_name)

    def offer_declined(self, offer):
        seller = offer.item.seller.user
        buyer = offer.buyer
        buyer_msg_title = f'{seller.username} declined your offer'
        buyer_msg_body = f'{buyer_msg_title} of {offer.amount} on {offer.item}'
        self.__notify(buyer, buyer_msg_title, buyer_msg_body)

    def offer_placed(self, offer):
        # WARNING: This should be provided from views instead of hardcoded here
        next_path_name = 'see-offers'
        seller = offer.item.seller.user
        buyer = offer.buyer
        seller_msg_title = f'{buyer} just placed an offer'
        seller_msg_body = f'{seller_msg_title} of {offer.amount} on {offer.item}'
        self.__notify(seller, seller_msg_title,
                      seller_msg_body, next_path_name)

    def __notify(self, user, title, body, next=None):
        inbox, created = self.manager.objects.get_or_create(user=user)
        self.model.objects.create(
            title=title,
            message=body,
            inbox=inbox
        )
        inbox.unread = F('unread') + 1
        inbox.save()
