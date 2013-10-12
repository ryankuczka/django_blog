from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from portfolio.forms import ContactForm
from blog.models import Entry
from projects.models import Project


def home(request):
    cxt = {}
    entries = Entry.objects.filter(published=True)[:3]
    cxt['entries'] = entries
    cxt['summary'] = True

    projects = Project.objects.filter(published=True)[:3]
    cxt['projects'] = projects
    return render(request, 'homepage.html', cxt)


def contact(request):

    cxt = {}
    if request.POST:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('contact_thanks'))
    else:
        form = ContactForm()

    cxt['form'] = form
    return render(request, 'contact_page.html', cxt)

def contact_thanks(request):
    return render(request, 'contact_thanks.html', {})
