import os

from .settings import *  # noqa

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = ["srv12.mikr.us"]
