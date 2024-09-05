# Generated by Django 5.1 on 2024-09-05 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0016_alter_image_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='focal_point',
            field=models.Field(blank=True, choices=[('top_left', 'Top Left'), ('top', 'Top'), ('top_right', 'Top Right'), ('center_left', 'Center Left'), ('center', 'Center'), ('center_right', 'Center Right'), ('bottom_left', 'Bottom Left'), ('bottom', 'Bottom'), ('bottom_right', 'Bottom Right')], null=True, verbose_name='Focal Point'),
        ),
    ]
