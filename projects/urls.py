from django.conf.urls import patterns, url

urlpatterns = patterns('projects.views',
    url(r'^$', 'index', name='projects_index'),
    url(r'^(?P<internal_name>[0-9a-z-_]+)', 'project_page', name='project_page'),
)
