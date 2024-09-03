from django.db import migrations
from django.utils.text import slugify

def add_slug_to_images(apps, schema_editor):
    Image = apps.get_model('gallery', 'Image')
    for image in Image.objects.all():
        if not image.slug:
            image.slug = slugify(image.title)
            image.save()

def add_slug_to_series(apps, schema_editor):
    Series = apps.get_model('gallery', 'Series')
    for series in Series.objects.all():
        if not series.slug:
            series.slug = slugify(series.title)
            series.save()

def add_slug_to_media(apps, schema_editor):
    Media = apps.get_model('gallery', 'Medium')
    for medium in Media.objects.all():
        if not medium.slug:
            medium.slug = slugify(medium.name)
            medium.save()

class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_image_slug_medium_slug_series_slug_and_more'),  # Replace with the actual previous migration file
    ]

    operations = [
        migrations.RunPython(add_slug_to_images),
        migrations.RunPython(add_slug_to_series),
        migrations.RunPython(add_slug_to_media),
    ]