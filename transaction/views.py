from django.shortcuts import render

# Create your views here.


def index(request):
    accepted_offers = request.user.offer_set.filter(status='pending')
    print(accepted_offers)
    return render(request, 'checkout/index.html', {'basket': accepted_offers})
