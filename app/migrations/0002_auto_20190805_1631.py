# Generated by Django 2.2.4 on 2019-08-05 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='test',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='timestamp',
        ),
    ]
