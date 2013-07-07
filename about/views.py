from about.models import AboutPage
from django.shortcuts import render


def index(request):
    """
    Index view of about pages
    """
    cxt = {}
    about_pages = AboutPage.objects.all()
    cxt['about_pages'] = about_pages

    return render(request, 'about/index.html', cxt)
