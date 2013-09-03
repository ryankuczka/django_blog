from about.models import AboutPage
from django.shortcuts import render


def index(request):
    return render(request, 'projects/projects_base.html', {})
