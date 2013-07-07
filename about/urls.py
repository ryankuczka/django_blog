from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^about/', 'about.views.index', name='about_index'),
    url(r'^about/(?P<internal_name>[0-9a-z_]+)', 'about.views.about_page', name='about_page'),
)
