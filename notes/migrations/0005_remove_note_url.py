# Generated by Django 2.1 on 2018-08-01 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20180731_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='url',
        ),
    ]
