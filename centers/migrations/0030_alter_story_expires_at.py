# Generated by Django 5.2.3 on 2025-07-18 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centers', '0029_alter_location_city_alter_location_region_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 7, 19, 11, 50, 13, 688434, tzinfo=datetime.timezone.utc)),
        ),
    ]
