from django import forms


class PersonUpdateForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    bio = forms.CharField(max_length=200)
    image = forms.ImageField()
