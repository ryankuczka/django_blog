from django.contrib import admin

from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'internal_name', 'updated',
        'published', 'source_control_link', 'external_link',
        'template_name')
admin.site.register(Project, ProjectAdmin)
