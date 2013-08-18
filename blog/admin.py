from django.contrib import admin
from django.db import models

from tinymce.widgets import TinyMCE
from blog.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'create_date', 'modify_date', 'publish_date')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }
admin.site.register(Entry, EntryAdmin)
