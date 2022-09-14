from random import choice, seed

from django.core.management import BaseCommand

from alerts.models import (
    CRIME_TYPE_CHOICES,
    CUSTOMER_SEGMENT_CHOICES,
    PRIORITY_CHOICES,
    PROJECT_CHOICES,
    SEVERITY_CHOICES,
    Alert,
)

PROJECTS = [x[0] for x in PROJECT_CHOICES]

# make command deterministic and set initial seed
seed(42)


def random_choice(choices):
    return choice([x[0] for x in choices])


def random_alert_data(project):
    return {
        "project": project,
        "customer_segment": random_choice(CUSTOMER_SEGMENT_CHOICES),
        "crime_type": random_choice(CRIME_TYPE_CHOICES),
        "priority": random_choice(PRIORITY_CHOICES),
        "severity": random_choice(SEVERITY_CHOICES),
    }


class Command(BaseCommand):
    def handle(self, *args, **options):
        # TODO: parametrize this later
        alerts_per_project = 300

        print(
            f"Number of alerts in db before running the command: {Alert.objects.count()}"
        )
        for project in PROJECTS:
            for _ in range(alerts_per_project):
                Alert.objects.create(**random_alert_data(project))

        print(f"Current number of alerts in db: {Alert.objects.count()}")
