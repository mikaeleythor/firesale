from django import forms


class PersonUpdateForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    bio = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={'cols': 60, 'rows': 5}))
    image = forms.ImageField()
