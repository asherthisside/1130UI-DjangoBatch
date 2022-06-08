# Generated by Django 4.0.4 on 2022-06-08 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_language_framework'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='guest',
            name='room',
            field=models.OneToOneField(default='N/A', on_delete=django.db.models.deletion.SET_DEFAULT, to='my_app.room'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('subjects', models.ManyToManyField(to='my_app.subject')),
            ],
        ),
    ]
