import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from about.models import AboutPage

PAGES = {
    'about_me': {
        'name': 'About Me',
        'template_name': 'about/about_me.html',
    },
    'education': {
        'name': 'Education',
        'template_name': 'about/education.html',
    },
    'experience': {
        'name': 'Experience',
        'template_name': 'about/experience.html',
    },
    'interests': {
        'name': 'Interests',
        'template_name': 'about/interests.html',
    },
}

for p, i in PAGES.items():
    AboutPage.objects.get_or_create(internal_name=p,
        defaults={
            'name': i['name'],
            'template_name': i['template_name'],
        }
    )
