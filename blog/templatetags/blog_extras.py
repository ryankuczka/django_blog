from django import template
from django.utils.datastructures import SortedDict

from blog.models import Entry

register = template.Library()


@register.inclusion_tag('blog/templatetags/sidebar_nav.html')
def blog_sidebar_nav():
    entries = Entry.objects.only('title', 'publish_date', 'internal_name')\
        .order_by('publish_date')
    entry_dict = SortedDict()
    for e in entries:
        menu = (e.title, e.get_absolute_url())
        if e.publish_date.year not in entry_dict:
            entry_dict.insert(0, e.publish_date.year, SortedDict(
                ((e.publish_date.strftime('%B'), [menu]),)
            ))
        elif e.publish_date.month not in entry_dict[e.publish_date.year]:
            entry_dict[e.publish_date.year][e.publish_date.strftime('%B')] = [menu]
        else:
            entry_dict[e.publish_date.year][e.publish_date.strftime('%B')].append(menu)
    return {'entry_dict': entry_dict}
