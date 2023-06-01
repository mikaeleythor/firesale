from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from item.forms.item_form import ItemCreateForm, ItemUpdateForm, ItemOfferForm
from item.models import Item, ItemImage, Seller, Offer
from notifications.interfaces import NotificationInterface
import json

notifyer = NotificationInterface()


def index(request):
    items = Item.objects.filter(status='Available').order_by('name')

    # NOTE: request.GET['invalidkey'] raises KeyError
    try:
        items = items.filter(name__icontains=request.GET['search_filter'])
    except KeyError:
        pass
    # NOTE: Enforcing default order_by name
    try:
        items = items.order_by(request.GET['order_by'])
    except KeyError:
        items = items.order_by('name')

    # NOTE: If any valid parameters were provided in request.GET
    if any([param in request.GET for param in ['order_by', 'search_filter']]):
        # NOTE: Change to list before responding
        items = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': str(x.itemimage_set.first().image.url)
        } for x in items]
        return JsonResponse({'data': items})
    context = {'items': items}
    return render(request, 'item/index.html', context)


def get_item_by_id(request, id):
    item = {'item': get_object_or_404(Item, pk=id)}
    similar = [{
        'id': x.id,
        'name': x.name,
        'price': x.price,
        'status': x.status,
        'firstImage': str(x.itemimage_set.first().image.url)
    } for x in Item.objects.filter(category__icontains=item['item'].category).exclude(id=item['item'].id)]
    if request.method == 'POST':
        form = ItemOfferForm(data=request.POST)
        if form.is_valid():
            offer = Offer.objects.create(**{
                'status': 'Pending',
                'amount': form.cleaned_data['amount'],
                'item': item['item'],
                'buyer': request.user
            })
            # NOTE: Notify seller
            notifyer.offer_placed(offer)
            form = ItemOfferForm()
    else:
        form = ItemOfferForm()

    current_highest_offer = 0
    offers = Offer.objects.filter(status='Pending')
    for offer in offers:
        if offer.item_id == id and offer.amount > current_highest_offer:
            current_highest_offer = offer.amount

    context = {'item': item, 'similar': similar,
               'form': form, 'current_highest_offer': current_highest_offer}
    return render(request, 'item/item_details.html', context)


def see_offers(request, id):
    item = get_object_or_404(Item, pk=id)
    offers = item.offer_set.filter(status='Pending')
    # HACK: Using content-type: application/json in template
    if request.method == 'POST':
        json_content = json.loads(request.body)
        if 'offerId' in json_content.keys():
            try:
                offerId = json_content['offerId']
                offer = get_object_or_404(Offer, pk=offerId)
                # NOTE: Input validated in model
                offer.status = json_content['status']
                offer.full_clean()
                offer.save()
                item = offer.item
                if json_content['status'] == 'Accepted':
                    item.status = "Waiting for payment"
                    item.full_clean()
                    item.save()
                    all_offers = item.offer_set.filter(status='Pending')
                    for decl_offer in all_offers:
                        if decl_offer.id != offer.id:
                            decl_offer.status = 'Declined'
                            offer.full_clean()
                            offer.save()
                            notifyer.offer_declined(decl_offer)
                    notifyer.offer_accepted(offer)
                    return JsonResponse(
                        status=200, data={"message": "Offer accepted"})
                if json_content['status'] == 'Declined':
                    notifyer.offer_declined(offer)
                    return JsonResponse(
                        status=200, data={"message": "Offer declined"})
            except ValidationError as error:
                return JsonResponse(
                    status=400, data={"message": str(error)})
        else:
            return JsonResponse(
                status=400, data={"message": "OfferId must be supplied"})
    return render(request, 'item/see_offers.html', {'offers': offers, 'item': item})


@login_required
def create_item(request):
    context = {}
    if request.user.person:
        if request.method == "POST":
            form = ItemCreateForm(data=request.POST)
            # NOTE: Failsafe to make sure images are provided
            #       Additional implementation needed in frontend for error msgs
            if form.is_valid() and request.FILES.getlist('images'):
                if (request.user.seller in Seller.objects.all()):
                    seller = Seller.objects.get(user=request.user)
                else:
                    seller = Seller.objects.create(user=request.user, rating=0)
                item = {
                    'name': form.cleaned_data['name'],
                    'status': 'Available',
                    'condition': form.cleaned_data['condition'],
                    'description': form.cleaned_data['description'],
                    'category': form.cleaned_data['category'],
                    'price': form.cleaned_data['price'],
                    'seller': seller,
                }
                itemObj = Item.objects.create(**item)

                images = request.FILES.getlist('images')
                for image in images:
                    imgObj = ItemImage.objects.create(
                        image=image, item=itemObj)
                    imgObj.save()
                return redirect('my-items')
        else:
            form = ItemCreateForm()
        context['form'] = form
        return render(request, 'item/create_item.html', context)
    else:
        return redirect("profile/create-person")


def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('item-index')


def update_item(request, id):
    instance = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        form = ItemUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('item-details', id=id)
    else:
        form = ItemUpdateForm(instance=instance)
    return render(request, 'item/update_item.html', {
        'form': form,
        'id': id
    })


def my_items(request):
    user_id = request.user.id
    items = Item.objects.filter(seller__user_id=user_id)
    return render(request, 'item/my_items.html', {'users_items_list': items})


def my_offers(request):
    user_id = request.user.id
    offers = Offer.objects.filter(buyer=user_id, status="Pending")
    items = []
    for offer in offers:
        items.append({'offer': offer.item, 'amount': offer.amount})
    return render(request, 'item/my_offers.html', {'users_offers_list': items})
