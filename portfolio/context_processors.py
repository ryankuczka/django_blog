
def site_section(request):
    site_section = ''
    path = request.path

    if path == '/':
        site_section = 'Home'
    elif '/about' in path:
        site_section = 'About'
    elif '/blog' in path:
        site_section = 'Blog'
    elif '/projects' in path:
        site_section = 'Projects'
    elif '/contact' in path:
        site_section = 'Contact'

    context = {'SITE_SECTION': site_section}

    return context
