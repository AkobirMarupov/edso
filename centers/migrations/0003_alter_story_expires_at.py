# Generated by Django 5.2.3 on 2025-06-17 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centers', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 18, 18, 30, 4, 757019, tzinfo=datetime.timezone.utc)),
        ),
    ]
