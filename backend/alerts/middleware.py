from time import sleep

from django.conf import settings


class RequestSleepMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        sleep(settings.REQUEST_SLEEP_SECONDS)
        return response
