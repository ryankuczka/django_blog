from django.contrib import admin
from about.models import AboutPage

class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'internal_name', 'template_name')
admin.site.register(AboutPage)
