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


def about_page(request, internal_name):
    """
    About page view
    """
    cxt = {}
    about_page = AboutPage.objects.get(internal_name=internal_name)
    cxt['about_page'] = about_page
    return render(request, about_page.template_name, cxt)
