# Generated by Django 5.1 on 2024-08-27 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_media_series'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Media',
            new_name='Medium',
        ),
    ]
