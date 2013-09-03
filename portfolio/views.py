from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from portfolio.forms import ContactForm


def home(request):
    return render(request, 'base_two_column.html', {})


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
