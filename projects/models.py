from django.db import models
from django.core.urlresolvers import reverse

import datetime


class Project(models.Model):
    name = models.CharField(max_length=200)
    internal_name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, default='')
    updated = models.DateTimeField(blank=True, null=True)
    source_control_link = models.URLField(blank=True, default='')
    external_link = models.URLField(blank=True, default='')
    template_name = models.CharField(max_length=200, blank=True, default='')
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ('-updated',)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('project_page', args=(self.internal_name,))
