import os

from dotenv import load_dotenv

from .settings import *  # noqa

load_dotenv()

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = ["srv12.mikr.us"]
