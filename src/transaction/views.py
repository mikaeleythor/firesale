from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from country_list import countries_for_language
import json
from item.models import Offer, SellerRating
from transaction.forms.checkout_form import PaymentForm
from notifications.interfaces import NotificationInterface


def has_accepted_offers(request) -> bool:
    return request.user.offer_set.filter(status='Accepted').exists()


@login_required
def index(request):
    if hasattr(request.user, 'person'):
        accepted_offers = request.user.offer_set.filter(status='Accepted')
        return render(
            request,
            'checkout/index.html',
            {'basket': accepted_offers}
        )
    return redirect("/profile/create-person")


@login_required
def contact_information(request):
    if hasattr(request.user, 'person'):
        # NOTE: User has to have some accepted offers to access this page
        if has_accepted_offers(request):
            countries = dict(countries_for_language('en'))
            return render(
                request,
                'checkout/contact_information.html',
                {'countries': countries.values()}
            )
        return render(request, '403_site.html')
    return redirect("/profile/create-person")


@login_required
def payment_information(request):
    if hasattr(request.user, 'person'):
        if has_accepted_offers(request):
            form = PaymentForm()
            return render(
                request, 'checkout/payment_information.html', {'form': form})
        return render(request, '403_site.html')
    return redirect("/profile/create-person")


@login_required
def review(request):
    if hasattr(request.user, 'person'):
        if has_accepted_offers(request):
            accepted_offers = request.user.offer_set.filter(status='Accepted')
            total = 0
            for item in accepted_offers:
                total += item.amount
            if request.method == 'POST':
                json_content = json.loads(request.body)
                if 'offerId' in json_content.keys():
                    try:
                        offerId = json_content['offerId']
                        offer = get_object_or_404(Offer, pk=offerId)
                        offer.status = 'Confirmed'
                        offer.full_clean()
                        offer.save()
                        item = offer.item
                        item.status = 'Sold'
                        item.full_clean()
                        item.save()
                        NotificationInterface().payment_received(
                            offer.buyer, item.seller.user, offer.amount, item)
                        return JsonResponse(
                            status=200, data={"message": "Item Sold"})
                    except ValidationError as error:
                        return JsonResponse(
                            status=400, data={"message": str(error)})
                else:
                    return JsonResponse(
                        status=400,
                        data={"message": "OfferId must be supplied"}
                    )
            return render(
                request,
                'checkout/review.html',
                {'basket': accepted_offers, 'total': total}
            )
        return render(request, '403_site.html')
    return redirect("/profile/create-person")


@login_required
def thank_you(request):
    if hasattr(request.user, 'person'):
        if request.method == 'POST':
            json_content = json.loads(request.body)
            if 'offerId' in json_content.keys():
                try:
                    offerId = json_content['offerId']
                    offer = get_object_or_404(Offer, pk=offerId)
                    seller = offer.item.seller
                    buyer = offer.buyer
                    SellerRating.objects.create(rating=json_content['rating'],
                                                seller=seller, buyer=buyer)
                    allratings = SellerRating.objects.filter(
                        seller=seller.id)
                    sum = 0
                    count = 0
                    for rating in allratings:
                        sum += rating.rating
                        count += 1
                    seller.rating = sum / count
                    seller.full_clean()
                    seller.save()
                    return JsonResponse(
                        status=200, data={"message": "Rating updated"})
                except ValidationError as error:
                    return JsonResponse(
                        status=400, data={"message": str(error)})
            else:
                return JsonResponse(
                    status=400, data={"message": "OfferId must be supplied"})
        return render(request, 'checkout/thank_you.html')
    return redirect("/profile/create-person")
