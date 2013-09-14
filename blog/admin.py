from django.contrib import admin

from blog.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'create_date', 'modify_date', 'publish_date')
admin.site.register(Entry, EntryAdmin)
