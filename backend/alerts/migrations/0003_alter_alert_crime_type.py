# Generated by Django 4.1.1 on 2022-09-14 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0002_alert_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='crime_type',
            field=models.CharField(choices=[('terrorism', 'terrorism'), ('money_laundering', 'money_laundering'), ('drug_trafficking', 'drug_trafficking'), ('cybercrime', 'cybercrime'), ('intelectual_property_crime', 'intelectual_property_crime'), ('corruption', 'corruption')], max_length=100),
        ),
    ]
