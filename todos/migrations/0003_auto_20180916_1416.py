# Generated by Django 2.1.1 on 2018-09-16 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20180916_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 16, 14, 16, 12, 840360)),
        ),
    ]
