# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'AboutPage.content'
        db.delete_column(u'about_aboutpage', 'content')


    def backwards(self, orm):
        # Adding field 'AboutPage.content'
        db.add_column(u'about_aboutpage', 'content',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    models = {
        u'about.aboutpage': {
            'Meta': {'object_name': 'AboutPage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['about']