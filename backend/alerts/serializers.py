from rest_framework import serializers

from . import models


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alert
        fields = (
            "id",
            "project",
            "severity",
            "customer_segment",
            "crime_type",
            "priority",
            "group_name",
        )


class CreateGroupSerializer(serializers.Serializer):
    name = serializers.CharField(allow_null=False)
    alert_ids = serializers.PrimaryKeyRelatedField(
        queryset=models.Alert.objects.all(),
        allow_null=False,
        allow_empty=False,
    )
