from blog.models import Entry
from django.utils.datastructures import SortedDict


def build_blog_date_dict():
    entries = Entry.objects.only('title', 'publish_date', 'internal_name')\
        .order_by('publish_date')
    entry_dict = SortedDict()
    for e in entries:
        month = '{:0>2}'.format(e.publish_date.month)
        month_name = e.publish_date.strftime('%B')
        if e.publish_date.year not in entry_dict:
            entry_dict.insert(0, e.publish_date.year, SortedDict(
                (((month, month_name), [e]),)
            ))
        elif (month, month_name) not in entry_dict[e.publish_date.year]:
            entry_dict[e.publish_date.year][(month, month_name)] = [e]
        else:
            entry_dict[e.publish_date.year][(month, month_name)].append(e)
    return entry_dict
