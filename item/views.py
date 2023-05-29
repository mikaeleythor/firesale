from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from item.forms.item_form import ItemCreateForm, ItemUpdateForm
from item.models import Item, ItemImage, Seller


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
    context = {'item': item, 'similar': similar}
    return render(request, 'item/item_details.html', context)


def see_offers(request, id):
    item = get_object_or_404(Item, pk=id)
    offers = item.offer_set.all()
    print(offers)
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
                'seller': Seller.objects.get_or_create(user=request.user)[0],
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
