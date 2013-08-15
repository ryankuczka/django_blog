from django import template

from blog.models import Entry
from blog.utils.blog_utils import build_blog_date_dict

register = template.Library()


@register.inclusion_tag('blog/templatetags/sidebar_nav.html', takes_context=True)
def blog_sidebar_nav(context):
    archive = context.get('archive', False)
    entry_dict = build_blog_date_dict()
    return {'entry_dict': entry_dict, 'archive': archive}
