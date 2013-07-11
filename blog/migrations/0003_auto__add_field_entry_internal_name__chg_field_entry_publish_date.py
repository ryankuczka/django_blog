# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entry.internal_name'
        db.add_column(u'blog_entry', 'internal_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


        # Changing field 'Entry.publish_date'
        db.alter_column(u'blog_entry', 'publish_date', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):
        # Deleting field 'Entry.internal_name'
        db.delete_column(u'blog_entry', 'internal_name')


        # Changing field 'Entry.publish_date'
        db.alter_column(u'blog_entry', 'publish_date', self.gf('django.db.models.fields.DateField')(null=True))

    models = {
        u'blog.entry': {
            'Meta': {'object_name': 'Entry'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modify_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']