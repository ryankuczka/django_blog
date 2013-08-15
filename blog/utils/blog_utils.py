from blog.models import Entry
from django.utils.datastructures import SortedDict


def build_blog_date_dict():
    entries = Entry.objects.only('title', 'publish_date', 'internal_name')\
        .order_by('publish_date')
    entry_dict = SortedDict()
    for e in entries:
        menu = (e.title, e.get_absolute_url())
        month_name = e.publish_date.strftime('%B')
        if e.publish_date.year not in entry_dict:
            entry_dict.insert(0, e.publish_date.year, SortedDict(
                ((e.publish_date.strftime('%B'), [menu]),)
            ))
        elif month_name not in entry_dict[e.publish_date.year]:
            entry_dict[e.publish_date.year][month_name] = [menu]
        else:
            entry_dict[e.publish_date.year][month_name].append(menu)
    return entry_dict