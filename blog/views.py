from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import Http404

from blog.models import Entry
from blog.utils.blog_utils import build_blog_date_dict

import datetime
import calendar
import logging
logger = logging.getLogger(__name__)


def index(request):
    """
    View which returns the three most recent posts
    """
    cxt = {}
    entries = Entry.objects.filter(published=True)
    entries = Paginator(entries, 3)

    cur_page = request.GET.get('p')
    try:
        entry_list = entries.page(cur_page)
    except PageNotAnInteger:
        entry_list = entries.page(1)
    except EmptyPage:
        entry_list = entries.page(entries.num_pages)

    cxt['entry_list'] = entry_list
    cxt['summary'] = True
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
    entries = Paginator(entries, 3)

    cur_page = request.GET.get('p')
    try:
        entry_list = entries.page(cur_page)
    except PageNotAnInteger:
        entry_list = entries.page(1)
    except EmptyPage:
        entry_list = entries.page(entries.num_pages)

    cxt['entry_list'] = entry_list
    cxt['summary'] = True
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
    cxt['summary'] = False
    return render(request, 'blog/entry.html', cxt)


def blog_archive(request):
    """
    View which displays all blogs by date
    """
    cxt = {}
    entry_dict = build_blog_date_dict()
    cxt['entry_dict'] = entry_dict
    cxt['archive'] = True
    return render(request, 'blog/archive.html', cxt)


def blog_by_tag(request, tag):
    """
    View which displays all blogs with a tag
    """
    cxt = {}
    entries = Entry.objects.filter(tags__slug=tag)
    entries = Paginator(entries, 3)

    cur_page = request.GET.get('p')
    try:
        entry_list = entries.page(cur_page)
    except PageNotAnInteger:
        entry_list = entries.page(1)
    except EmptyPage:
        entry_list = entries.page(entries.num_pages)

    cxt['entry_list'] = entry_list
    cxt['tags'] = True
    cxt['summary'] = True
    return render(request, 'blog/entry_list.html', cxt)
