from django_filters import rest_framework as filters

from .models import Alert


class AlertFilter(filters.FilterSet):
    class Meta:
        model = Alert
        fields = {
            "project": ["exact"],
            "severity": ["exact"],
            "customer_segment": ["exact"],
            "crime_type": ["exact"],
            "priority": ["exact"],
            "group_name": ["exact", "isnull"],
        }
