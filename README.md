# Moroccan Association for YES Alumni

This is the official repository for the website of YES Alumni Morocco

Currently hosted on Azure Web Apps via [yesalumni-morocco.azurewebsites.net](https://yesalumni-morocco.azurewebsites.net/).

## Technologies Used
- [Django](https://docs.djangoproject.com/en/5.0/)
- [Django Jazzmin](https://django-jazzmin.readthedocs.io/)
- [TailwindCSS](https://tailwindcss.com/docs/installation)
- [Preline UI](https://preline.co/docs/index.html)
- [Lucide Icons](https://lucide.dev/guide/)
- [Open Graph](https://ogp.me/)
- [Azure Web Apps](https://azure.microsoft.com/en-us/products/app-service/web)
- [Azure Storage Accounts](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)

## Getting Started
To use this template to start your own project:

First clone the repository from Github and switch to the new directory:
```bash
git clone https://github.com/aabboudi/yesalumni-morocco.git
cd .\yesalumni-morocco\
```

Create or activate the virtual environment for your project:
```bash
virtualenv venv
.\venv\Scripts\activate
```

Install project dependencies:
```bash
pip install -r requirements.txt
```

Install UI dependencies:
```bash
cd .\ui\
npm install
cd ..
```

Make and apply all migrations:
```bash
py manage.py makemigrations
py manage.py migrate
```

Make sure `STATIC_ROOT` is defined in `settings.py` and collect all static files in order for styles to work:
```bash
py manage.py collectstatic
```

Create a superuser to access the admin interface:
```bash
py manage.py createsuperuser
```

You can now run the development server:
```bash
py manage.py runserver
```
