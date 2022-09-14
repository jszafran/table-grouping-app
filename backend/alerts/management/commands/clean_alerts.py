from django.core.management import BaseCommand

from alerts.models import Alert


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(f"Deleting {Alert.objects.count()} alert(s).")
        Alert.objects.all().delete()
        print("Done!")
