from django.shortcuts import render

# Create your views here.


def index(request):
    accepted_offers = request.user.offer_set.filter(status='Accepted')
    return render(request, 'checkout/index.html', {'basket': accepted_offers})


def contact_information(request):
    if request.method == 'POST':
        request.session['contact_info'] = {
            'full_name': request.POST.get('full_name'),
            'city': request.POST.get('city')
        }

    return render(request, 'checkout/contact_information.html')
