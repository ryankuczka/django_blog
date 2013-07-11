from about.models import AboutPage
from django.shortcuts import render


def home(request):
    return render(request, 'base_two_column.html', {})
