from django import forms
from django.forms import ModelForm, widgets, Form
from item.models import Item
category_choice = [('Category', 'Category'),
                   ('Electronics', 'Electronics'),
                   ('Fashion', 'Fashion'),
                   ('Home & Kitchen', 'Home & Kitchen'),
                   ('Beauty & Personal Care', 'Beauty & Personal Care'),
                   ('Toys & Games', 'Toys & Games'),
                   ('Books', 'Books'),
                   ('Sports & Outdoors', 'Sports & Outdoors')
                   ]


class ItemCreateForm(forms.ModelForm):
    name = forms.CharField(
        label="", max_length=25, widget=forms.TextInput(
            attrs={'placeholder': 'Name'}))
    condition = forms.CharField(
        label="", max_length=40, widget=forms.TextInput(
            attrs={'placeholder': 'Condition'}))
    price = forms.CharField(
        label="", max_length=40, widget=forms.TextInput(
            attrs={'placeholder': 'Price'}))
    category = forms.ChoiceField(
        choices=category_choice, label="", widget=forms.Select)
    description = forms.CharField(
        label="", max_length=200, widget=forms.TextInput(
            attrs={'placeholder': 'Description'}))

    class Meta:
        model = Item
        exclude = ['id', 'seller', 'status']


class ItemUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=25, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    condition = forms.CharField(
        max_length=40, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    price = forms.CharField(
        max_length=40, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices=category_choice, widget=forms.Select)
    description = forms.CharField(
        max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    class Meta:
        model = Item
        exclude = ['id', 'seller', 'status']


class ItemOfferForm(Form):
    amount = forms.IntegerField(
        min_value=1, max_value=9999999, label="", widget=forms.NumberInput(
            attrs={'placeholder': 'Input offer...'}))
