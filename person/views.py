from django.shortcuts import render
# Create your views here.

persons = [
    {'name': 'smarties', 'price': 100},
    {'name': 'skittles', 'price': 200}
]


def index(request):
    return render(request, 'person/index.html', context={'persons': persons})
