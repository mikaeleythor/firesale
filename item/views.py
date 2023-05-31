from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from item.forms.item_form import ItemCreateForm, ItemUpdateForm, ItemOfferForm
from item.models import Item, ItemImage, Seller, Offer
from notifications.interfaces import NotificationInterface
import json

notifyer = NotificationInterface()


def index(request):
    items = Item.objects.all().order_by('name')
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

    # NOTE: If any parameters were provided in request.GET
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
        'firstImage': str(x.itemimage_set.first().image.url)
    } for x in Item.objects.filter(category__icontains=item['item'].category).exclude(id=item['item'].id)]
    if request.method == 'POST':
        form = ItemOfferForm(data=request.POST)
        if form.is_valid():
            offer = Offer.objects.create(**{
                'status': 'pending',
                'amount': form.cleaned_data['amount'],
                'item': item['item'],
                'buyer': request.user
            })
            # NOTE: Notify seller
            notifyer.offer_placed(offer)
    else:
        form = ItemOfferForm()
    context = {'item': item, 'similar': similar, 'form': form}
    return render(request, 'item/item_details.html', context)


def see_offers(request, id):
    item = get_object_or_404(Item, pk=id)
    offers = item.offer_set.all()
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
                item.status = "Waiting for payment"
                item.full_clean()
                item.save()
                notifyer.offer_accepted(offer)
                return JsonResponse(
                    status=200, data={"message": "Offer accepted"})
            except ValidationError as error:
                return JsonResponse(
                    status=400, data={"message": str(error)})
        else:
            return JsonResponse(
                status=400, data={"message": "OfferId must be supplied"})
    return render(request, 'item/see_offers.html', {'offers': offers})


def create_item(request):
    context = {}
    if request.method == "POST":
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = {
                'name': form.cleaned_data['name'],
                'status': 'Available',
                'condition': form.cleaned_data['condition'],
                'description': form.cleaned_data['description'],
                'category': form.cleaned_data['category'],
                'price': form.cleaned_data['price'],
                'seller': Seller.objects.get_or_create(user=request.user, rating=0)[0],
            }
            itemObj = Item.objects.create(**item)

            images = request.FILES.getlist('images')
            for image in images:
                imgObj = ItemImage.objects.create(image=image, item=itemObj)
                imgObj.save()
            return redirect('item-index')
    else:
        form = ItemCreateForm()
    context['form'] = form
    return render(request, 'item/create_item.html', context)


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
