from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, views
from rest_framework.response import Response

from .filters import AlertFilter
from .models import Alert
from .serializers import AddGroupSerializer, AlertSerializer, RemoveGroupSerializer


class AlertsListView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()
    filterset_class = AlertFilter


class AddGroupAPIView(views.APIView):
    def post(self, request):
        serializer = AddGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Alert.objects.filter(pk__in=serializer.data["alert_ids"]).update(
            group_name=serializer.data["group_name"],
        )
        return Response(status=status.HTTP_200_OK)


class RemoveGroupAPIView(views.APIView):
    def post(self, request):
        serializer = RemoveGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Alert.objects.filter(
            project=serializer.data["project"],
            group_name=serializer.data["group_name"],
        ).update(group_name=None)
        return Response(status=status.HTTP_200_OK)
