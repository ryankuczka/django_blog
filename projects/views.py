from projects.models import Project
from django.shortcuts import render


def index(request):
    return render(request, 'projects/projects_base.html', {})


def project_page(request, internal_name):
    cxt = {}
    try:
        project = Project.objects.get(internal_name=internal_name)
    except Project.DoesNotExist:
        return render(request, 'projects/projects_base.html', {})
    cxt['project'] = project
    return render(request, 'projects/project_page.html', cxt)
