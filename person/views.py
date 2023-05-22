from django.shortcuts import render
from django.http import HttpResponse


# TODO: Implement render(template)
def index(request):
    return HttpResponse("Response from ProfileView")
