# Generated by Django 5.1 on 2024-09-05 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0016_alter_image_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_focal_point',
            field=models.CharField(blank=True, choices=[('', 'Focal Point'), ('bottom', 'Bottom Center'), ('bottom_left', 'Bottom Left'), ('bottom_right', 'Bottom Right'), ('center', 'Center'), ('left', 'Center Left'), ('right', 'Center Right'), ('top', 'Top Center'), ('top_left', 'Top Left'), ('top_right', 'Top Right')], max_length=255, null=True),
        ),
    ]
