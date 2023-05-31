from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="checkout"),
    path('contact-information', views.contact_information,
         name="contact-information"),
    path('payment-information', views.payment_information,
         name="payment-information"),
    path('review', views.review,
         name="review"),
    path('thank-you', views.thank_you, name='thank-you')

]
