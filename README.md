# scraping_test_task
There is no need to make request/bs4 because "brain.com.ua" is js loaded site

## django API Setup
making venv:
```shell
python -m venv venv
```

Activating venv:
```shell
.\venv_win\Scripts\activate
```

Then installing Django and restframework:
```shell
pip install django
pip install django djangorestframework
pip install psycopg2-binary
```

Making our project:
```shell
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
```

In `myproject/settings.py` adding your app

In `myproject/settings.py` edit DATABASES:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "example",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

