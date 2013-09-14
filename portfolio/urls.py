from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^portfolio/', include('portfolio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', include('about.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^contact/$', 'portfolio.views.contact', name='contact'),
    url(r'^contact/thanks', 'portfolio.views.contact_thanks', name='contact_thanks'),
)
