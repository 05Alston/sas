# Generated by Django 4.0.5 on 2022-07-10 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cls', '0002_class_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='course',
        ),
        migrations.RemoveField(
            model_name='class',
            name='is_timetable',
        ),
    ]
