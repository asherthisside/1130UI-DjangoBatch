# Generated by Django 4.0.4 on 2022-05-17 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=40)),
                ('qualification', models.CharField(max_length=20)),
                ('salary', models.FloatField()),
            ],
        ),
    ]