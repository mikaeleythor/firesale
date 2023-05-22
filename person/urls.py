from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/person
    path('', views.index, name="person-index"),
]
