from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from item.forms.item_form import ItemCreateForm, ItemUpdateForm
from item.models import Item, ItemImage

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        items = [ {
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': str(x.itemimage_set.first().image.url)
        } for x in Item.objects.filter(name__icontains=search_filter)]
        return JsonResponse({ 'data': items })
    context = {'items': Item.objects.all().order_by('name')}
    return render(request, 'item/index.html', context)

def get_item_by_id(request, id):
    item = {'item': get_object_or_404(Item, pk=id)}
    similar = [ {
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': str(x.itemimage_set.first().image.url)
        } for x in Item.objects.filter(category__icontains=item['item'].category)]
    context = {'item': item, 'similar': similar}
    return render(request, 'item/item_details.html', context)

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
