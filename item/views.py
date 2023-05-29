from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from item.forms.item_form import ItemCreateForm, ItemUpdateForm, ItemOfferForm
from item.models import Item, ItemImage, Offer


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        items = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': str(x.itemimage_set.first().image.url)
        } for x in Item.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': items})
    if 'order_by' in request.GET:
        order_by = request.GET['order_by']
        items = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': str(x.itemimage_set.first().image.url)
        } for x in Item.objects.order_by(order_by)]
        return JsonResponse({'data': items})
    context = {'items': Item.objects.all().order_by('name')}
    return render(request, 'item/index.html', context)


def get_item_by_id(request, id):
    item = {'item': get_object_or_404(Item, pk=id)}
    similar = [{
        'id': x.id,
        'name': x.name,
        'price': x.price,
        'firstImage': str(x.itemimage_set.first().image.url)
    } for x in Item.objects.filter(category__icontains=item['item'].category)]
    if request.method == 'POST':
        form = ItemOfferForm(data=request.POST)
        if form.is_valid():
            offer = Offer.objects.create(**{
                'status': 'pending',
                'amount': form.cleaned_data['amount'],
                'item': item['item'],
                'buyer': request.user
            })
    else:
        form = ItemOfferForm()
    context = {'item': item, 'similar': similar, 'form': form}
    return render(request, 'item/item_details.html', context)

def see_offers(request, id):
    item = get_object_or_404(Item, pk=id)
    offers = item.offer_set.all()
    print(offers)
    return render(request, 'item/see_offers.html', {'offers': offers})


def create_item(request):
    if request.method == 'POST':
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = form.save()
            item_image = ItemImage(image=request.POST['image'], item=item)
            item_image.save()
            return redirect('item-index')
    else:
        form = ItemCreateForm()
    return render(request, 'item/create_item.html', {
        'form': form
    })


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

# def place_offer(request, id):
#     item = get_object_or_404(Item, pk=id)
#     if request.method == 'POST':
#         form = ItemOfferForm(data=request.POST)
#         if form.is_valid():
#             offer = Offer.objects.create(
#             status='pending',
#             amount =form.cleaned_data['amount'],
#             item = item,
#             buyer = request.user.id)
#         else:
#             form = ItemOfferForm()
#         return render(request, 'item/item_details.html', {
#         'form': form, 'item': item
#     })

# #  amount = form.save()
# #             offer = Offer.objects.create(
# #                 status='pending',
# #                 amount=amount,
# #                 item=item,
# #                 buyer=request.user