from django.db import models
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager

import re
import datetime


AUTHORS = (
    ('ryan_kuczka', 'Ryan Kuczka'),
)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    internal_name = models.CharField(max_length=200)
    template_name = models.CharField(max_length=200, default='posts/lorem_ipsum.html')
    author = models.CharField(max_length=50, choices=AUTHORS)
    published = models.BooleanField(blank=True, default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateField(default=datetime.date.today)
    tags = TaggableManager()

    class Meta:
        ordering = ('publish_date',)
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return u'%s' % self.title

    def publish(self):
        self.published = True
        self.publish_date = datetime.date.today()

    def get_absolute_url(self):
        year = '{}'.format(self.publish_date.year)
        month = '{:0>2}'.format(self.publish_date.month)
        day = '{:0>2}'.format(self.publish_date.day)
        kwargs = {
            'year': year,
            'month': month,
            'day': day,
            'internal_name': self.internal_name,
        }
        return reverse('blog_entry', kwargs=kwargs)

    @property
    def get_intro_para(self):
        """
        Simply returns the first <p></p> block... for now
        """
        first_para = re.search(r'^<p.*?>(?P<first_para>.*?)</p>', self.content)
        if first_para:
            first_para_text = first_para.group('first_para')
            return first_para_text
        else:
            return self.content
