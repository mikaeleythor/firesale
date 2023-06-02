from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, '404_site.html', status=404)
