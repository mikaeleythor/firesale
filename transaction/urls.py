from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="transaction-index"),
    path('contact-information', views.contact_information,
         name="contact-information")
]
