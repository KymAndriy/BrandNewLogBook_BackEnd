# Generated by Django 2.2.11 on 2020-05-22 00:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learnGroups', '0003_auto_20200521_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learngroup',
            name='ends_on',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='learngroup',
            name='start_on',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
