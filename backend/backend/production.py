import os

from .settings import *  # noqa

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = [
    "srv12.mikr.us",
    "srv12.mikr.us:20421",
]

DEBUG = False

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ("rest_framework.renderers.JSONRenderer",)

try:
    REQUEST_SLEEP_SECONDS = float(os.getenv("REQUEST_SLEEP_SECONDS"))
except (ValueError, TypeError):
    REQUEST_SLEEP_SECONDS = 0.0
