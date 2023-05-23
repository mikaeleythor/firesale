from django import forms
from django.forms import ModelForm, widgets
from item.models import Item


class ItemCreateForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={ 'class':'form-control' }))
    class Meta:
        model = Item
        exclude = [ 'id', 'seller', 'status']
        widgets = {
            'name': widgets.TextInput(attrs={ 'class':'form-control' }),
            'description': widgets.TextInput(attrs={ 'class':'form-control' }),
            'category': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.TextInput(attrs={ 'class':'form-control' }),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class ItemUpdateForm(ModelForm):
    class Meta:
        model = Item
        exclude = [ 'id', 'seller', 'status']
        widgets = {
            'name': widgets.TextInput(attrs={ 'class':'form-control' }),
            'description': widgets.TextInput(attrs={ 'class':'form-control' }),
            'category': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.TextInput(attrs={ 'class':'form-control' }),
            'condition': widgets.TextInput(attrs={'class': 'form-control'}),
        }