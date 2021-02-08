"""
Django settings for handyman project.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/


For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/

"""
from os import environ

import django_stubs_ext
from split_settings.tools import include

# Monkeypatching Django, so stubs will work for all generics,
# see: https://github.com/typeddjango/django-stubs
django_stubs_ext.monkeypatch()

environ.setdefault("DJANGO_ENV", "development")
ENV = environ["DJANGO_ENV"]

_base_settings = (
    "components/common.py",
    f"environments/{ENV}.py",
)

# Include settings:
include(*_base_settings)
