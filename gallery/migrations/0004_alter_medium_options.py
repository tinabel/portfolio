# Generated by Django 5.1 on 2024-08-27 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_rename_media_medium'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medium',
            options={'verbose_name_plural': 'media'},
        ),
    ]
