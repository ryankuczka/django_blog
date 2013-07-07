from django.db import models

class AboutPage(models.Model):

    name = models.CharField(max_length=200)
    internal_name = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    template_name = models.CharField(max_length=70)

    def __unicode__(self):
        return '%s' % self.name
