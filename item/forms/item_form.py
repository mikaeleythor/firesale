from django import forms
from django.forms import ModelForm, widgets, Form
from item.models import Item

class ItemCreateForm(forms.ModelForm):
    name = forms.CharField(label="",max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    condition = forms.CharField(label="",max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Condition'}))
    price = forms.CharField(label="",max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Price'}))
    category = forms.CharField(label="",max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Category'}))
    description = forms.CharField(label="",max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    class Meta:
        model = Item
        exclude = ['id', 'seller', 'status']


class ItemUpdateForm(ModelForm):
    name = forms.CharField(label="",max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}))
    condition = forms.CharField(label="",max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.CharField(label="",max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.CharField(label="",max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label="",max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    class Meta:
        model = Item
        exclude = ['id', 'seller', 'status']

class ItemOfferForm(Form):
    amount = forms.IntegerField(min_value=1,max_value=9999999, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Input offer...'}))
