from django.db import models

PROJECT_CHOICES = (
    (
        "LB_PROJ_GB",
        "LB_PROJ_GB",
    ),
    (
        "BT_PROJ_AU",
        "LB_PROJ_GB",
    ),
    (
        "LB_PROJ_IT",
        "LB_PROJ_GB",
    ),
)


SEVERITY_CHOICES = (
    ("high", "high"),
    ("medium", "medium"),
    ("low", "low"),
)


CUSTOMER_SEGMENT_CHOICES = (
    ("enterprise", "enterprise"),
    ("private", "private"),
)


CRIME_TYPE_CHOICES = (
    ("terrorism", "terrorism"),
    ("money laundering", "money laundering"),
    ("drug trafficking", "drug trafficking"),
    ("cybercrime", "cybercrime"),
    ("intelectual property crime", "intelectual property crime"),
    ("corruption", "corruption"),
)


PRIORITY_CHOICES = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
)


class CreatedModifiedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Alert(CreatedModifiedMixin, models.Model):
    project = models.CharField(max_length=100, choices=PROJECT_CHOICES)
    severity = models.CharField(max_length=100, choices=SEVERITY_CHOICES)
    customer_segment = models.CharField(
        max_length=100, choices=CUSTOMER_SEGMENT_CHOICES
    )
    crime_type = models.CharField(max_length=100, choices=CRIME_TYPE_CHOICES)
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES)
