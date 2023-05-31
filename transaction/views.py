from django.shortcuts import render
from country_list import countries_for_language

from transaction.forms.checkout_form import PaymentForm

# Create your views here.


def index(request):
    accepted_offers = request.user.offer_set.filter(status='Accepted')
    return render(request, 'checkout/index.html', {'basket': accepted_offers})


def contact_information(request):
    countries = dict(countries_for_language('en'))
    return render(request, 'checkout/contact_information.html', {'countries': countries.values()})


def payment_information(request):
    form = PaymentForm()
    return render(request, 'checkout/payment_information.html', {'form': form})


def review(request):
    accepted_offers = request.user.offer_set.filter(status='Accepted')
    total = 0
    for item in accepted_offers:
        total += item.amount
    return render(request, 'checkout/review.html', {'basket': accepted_offers, 'total': total})


def thank_you(request):
    return render(request, 'checkout/thank_you.html')


def notify_buyer_with_seller_ratings():
    bla = ''
    # pass
