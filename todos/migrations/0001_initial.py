# Generated by Django 2.1.1 on 2018-09-15 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(blank=models.TextField(), default=datetime.datetime(2018, 9, 16, 1, 18, 7, 787988))),
            ],
        ),
    ]
