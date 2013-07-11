from django.db import models


AUTHORS = (
    ('ryan_kuczka', 'Ryan Kuczka'),
)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=50, choices=AUTHORS)
    published = models.BooleanField(blank=True, default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.title
