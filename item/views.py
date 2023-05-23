from django.shortcuts import render, get_object_or_404
from item.models import Item


def index(request):
    context = {'items': Item.objects.all().order_by('name')}
    return render(request, 'item/index.html', context)

def get_item_by_id(request, id):
    return render(request, 'item/item_details.html', {
        'item': get_object_or_404(Item, pk=id)
    })