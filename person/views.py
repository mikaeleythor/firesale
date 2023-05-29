from django.shortcuts import render, redirect, get_object_or_404
from person.models import Person
from person.forms.person_form import PersonUpdateForm
from django.contrib.auth.models import User


def index(request):
    context = {'person': Person.objects.get(user=request.user)}
    return render(request, 'person/index.html', context)


def update_person(request):
    id = request.user.person.id
    if request.method == 'POST':
        form = PersonUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            Person.objects.filter(id=id).update(
                bio=form.cleaned_data['bio'],
                image=form.cleaned_data.get('image')
            )
            User.objects.filter(id=request.user.id).update(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            return redirect('person-index')
    else:
        form = PersonUpdateForm()
    return render(request, 'person/update_profile.html', {
        'form': form,
        'id': id
    })
