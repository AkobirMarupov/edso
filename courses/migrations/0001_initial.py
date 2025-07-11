# Generated by Django 5.2.3 on 2025-06-16 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('centers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=400, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.CharField(choices=[('3 oy', '3 oy'), ('6 oy', '6 oy'), ('8 0y', '8 oy')], default='vaqt1', max_length=20)),
                ('price', models.BigIntegerField()),
                ('language', models.CharField(blank=True, max_length=100, null=True)),
                ('schedule', models.CharField(choices=[('3 kun', '3 kun'), ('5 kun', '5 kun')], default='kun1', max_length=20)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='courses', to='centers.center')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
