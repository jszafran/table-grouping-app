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


class AddGroupSerializer(serializers.Serializer):
    group_name = serializers.CharField(allow_null=False)
    alert_ids = serializers.PrimaryKeyRelatedField(
        queryset=models.Alert.objects.all(),
        allow_null=False,
        allow_empty=False,
        many=True,
    )


class RemoveGroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["group_name", "project"]
        model = models.Alert
