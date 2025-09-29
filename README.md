# scraping_test_task
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
```

Making our project:
```shell
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
```

In `myproject/settings.py` adding our apps:
```python

```