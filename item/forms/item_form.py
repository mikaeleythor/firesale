from django import forms
from django.forms import ModelForm, widgets
from item.models import Item, ItemImage


class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['id', 'seller', 'status']
        labels = {
            'name': "",
            'condition': "",
            'price': "",
            'category': "",
            'description': ""
        }
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control','placeholder': 'Condition'}),
            'price': widgets.TextInput(attrs={'class': 'form-control','placeholder': 'Price'}),
            'category': widgets.TextInput(attrs={'class': 'form-control','placeholder': 'Category'}),
            'description': widgets.TextInput(attrs={'class': 'form-control','placeholder': 'Description'}),
        }

class ItemImageCreateForm(ModelForm):
    class Meta:
        model = ItemImage
        exclude = ['id', 'item']
        
        widgets = {
            'image': forms.ImageField(label="", required=True, widget=forms.TextInput(
            attrs={'class': 'form-control','placeholder': '+ Add image'}))
        }


class ItemUpdateForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['id', 'seller', 'status']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.TextInput(attrs={'class': 'form-control'}),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
        }
