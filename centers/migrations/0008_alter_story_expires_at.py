# Generated by Django 5.2.3 on 2025-06-18 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centers', '0007_alter_story_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 6, 19, 12, 47, 47, 601645, tzinfo=datetime.timezone.utc)),
        ),
    ]
