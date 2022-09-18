import os

from dotenv import load_dotenv

from .settings import *  # noqa

load_dotenv()

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = [
    "srv12.mikr.us",
    "srv12.mikr.us:20421",
]

DEBUG = False

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ("rest_framework.renderers.JSONRenderer",)
