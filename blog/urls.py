from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='blog_index'),
    url(r'^(?P<year>\d{4})/$', 'blog.views.blog_by_date', name='blog_by_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'blog.views.blog_by_date', name='blog_by_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'blog.views.blog_by_date',
        name='blog_by_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<internal_name>[0-9a-z_]+)$',
        'blog.views.entry', name='blog_entry'),
    url(r'^archive$', 'blog.views.blog_archive', name='blog_archive'),
    url(r'^tag/(?P<tag>[A-Za-z0-9-_]+)', 'blog.views.blog_by_tag', name='blog_by_tag'),
)
