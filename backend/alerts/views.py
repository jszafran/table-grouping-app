from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Alert
from .serializers import AlertSerializer


class AlertsListView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()
