# Generated by Django 4.0.4 on 2022-05-26 05:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_one', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 10, 53, 50, 924794)),
        ),
    ]
