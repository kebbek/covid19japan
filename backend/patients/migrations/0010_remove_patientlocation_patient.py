# Generated by Django 3.0.3 on 2020-03-06 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0009_auto_20200307_0137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientlocation',
            name='patient',
        ),
    ]
