from dataclasses import fields
from django import forms
from django.forms import ModelForm, widgets
from person.models import Person
from django.contrib.auth.models import User


class PersonUpdateForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    bio = forms.CharField(max_length=200)
    image = forms.ImageField()
