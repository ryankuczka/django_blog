# Portfolio Blog
## Setup
### Clone the Repo

```bash
git clone git@bitbucket.org:rkuczka/portfolio.git
cd portfolio
```

### Set Up virtualenv

```bash
mkvirtualenv --distribute portfolio
pip install -r requirements/dev.txt
```

### Set up database

```bash
python manage.py sync_db
python manage.py migrate
```

### Add about Pages

```bash
export DJANGO_SETTINGS_MODULE='portfolio.settings'
python about/onetime_scripts/create_about_pages.py
```
