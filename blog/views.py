from django.shortcuts import render
from django.http import Http404
from blog.models import Entry

import datetime
import calendar


def index(request):
    """
    View which returns the three most recent posts
    """
    cxt = {}
    entries = Entry.objects.filter(published=True).order_by('-publish_date')[:3]
    cxt['entries'] = entries
    return render(request, 'blog/entry_list.html', cxt)


def blog_by_date(request, year, month=None, day=None):
    """
    View which returns all entries by year
    """
    cxt = {}
    year = int(year)
    if month is None:
        start_date = datetime.date(year, 1, 1)
        end_date = datetime.date(year, 12, 31)
    elif day is None:
        month = int(month)
        start_date = datetime.date(year, month, 1)
        end_date = datetime.date(year, month, calendar.monthrange(year, month)[1])
    else:
        month = int(month)
        day = int(day)
        start_date = datetime.date(year, month, day)
        end_date = datetime.date(year, month, day)
    entries = Entry.objects.filter(published=True)\
        .filter(publish_date__gte=start_date)\
        .filter(publish_date__lte=end_date)
    cxt['entries'] = entries
    return render(request, 'blog/entry_list.html', cxt)


def entry(request, year, month, day, internal_name):
    """
    View for a blog entry
    """
    cxt = {}
    date = datetime.date(int(year), int(month), int(day))
    entry = Entry.objects.get(internal_name=internal_name, publish_date=date)
    if entry.published is False:
        raise Http404
    cxt['entry'] = entry
    return render(request, 'blog/entry.html', cxt)
