# Generated by Django 2.2.11 on 2020-05-26 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_lesson_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='teacher',
            new_name='teacher_id',
        ),
    ]
