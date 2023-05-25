from django.shortcuts import render
from person.models import Person
# Create your views here.

# persons = [
#     {'name': 'smarties', 'price': 100},
#     {'name': 'skittles', 'price': 200}
# ]


def index(request):
    # context = {'persons': persons}
    # return render(request, 'person/index.html', context)
    context = {'persons': Person.objects.all()}
    return render(request, 'person/index.html', context)
