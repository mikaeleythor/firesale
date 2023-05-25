from django.shortcuts import render
from person.models import Person


def index(request):
    # context = {'persons': persons}
    # return render(request, 'person/index.html', context)

    context = {'persons': Person.objects.all()}
    return render(request, 'person/index.html', context)
