# Generated by Django 4.0.5 on 2022-09-02 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_remove_teacherprofile_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=20, verbose_name='Class Name')),
                ('department', models.CharField(blank=True, choices=[('Computer Engineering', 'Computer Engineering'), ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'), ('Information Technology', 'Information Technology'), ('Mechanical Engineering', 'Mechanical Engineering')], max_length=100, null=True)),
                ('class_teacher', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.teacherprofile')),
            ],
            options={
                'verbose_name_plural': 'classes',
            },
        ),
    ]
