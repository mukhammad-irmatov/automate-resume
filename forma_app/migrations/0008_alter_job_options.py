# Generated by Django 3.2.9 on 2021-12-09 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forma_app', '0007_job_jobdate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['JobDate']},
        ),
    ]
