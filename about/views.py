from about.models import AboutPage
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    """
    Index view of about pages
    """
    return HttpResponseRedirect(reverse('about_page', args=('about_me',)))


def about_page(request, internal_name):
    """
    About page view
    """
    cxt = {}
    about_page = AboutPage.objects.get(internal_name=internal_name)
    cxt['about_page'] = about_page
    return render(request, 'about/about_page.html', cxt)
