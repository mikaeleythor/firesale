from django import forms
from django.forms import ModelForm, widgets, Form
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
            'name': widgets.TextInput(attrs={'placeholder': 'Name'}),
            'condition': widgets.TextInput(attrs={'placeholder': 'Condition'}),
            'price': widgets.TextInput(attrs={'placeholder': 'Price'}),
            'category': widgets.TextInput(attrs={'placeholder': 'Category'}),
            'description': widgets.TextInput(attrs={'placeholder': 'Description'}),
        }


class ItemCreateImageForm(forms.Form):
    image = forms.ImageField()


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
