from django_filters import rest_framework as filters

from .models import Alert


class AlertFilter(filters.FilterSet):
    class Meta:
        model = Alert
        fields = {
            "project": ["exact"],
            "severity": ["exact", "in"],
            "customer_segment": ["exact", "in"],
            "crime_type": ["exact", "in"],
            "priority": ["exact", "in"],
            "group_name": ["exact", "isnull", "in"],
        }
