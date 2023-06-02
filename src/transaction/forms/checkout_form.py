from django.forms import CharField, Form, IntegerField

from dj_cleavejs import *


class PaymentForm(Form):
    creditcard = IntegerField(widget=CreditCard())
    date = CharField(widget=CleaveWidget(blocks=[2, 2], delimiter="/"))
    cvc = CharField(widget=CleaveWidget(blocks=[3]))
