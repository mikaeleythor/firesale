from django.shortcuts import render

def page_not_found_view(request):
    return render(request, '404_site.html', status=404)