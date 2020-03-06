# Generated by Django 3.0.3 on 2020-03-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_auto_20200306_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
