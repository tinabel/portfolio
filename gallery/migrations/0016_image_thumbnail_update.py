
from django.db import migrations, models
from gallery.image_utility import ImageUtility

def add_thumbnail_to_images(apps, schema_editor):
    Image = apps.get_model('gallery', 'Image')
    for image in Image.objects.all():
      if image.image_file and not image.thumbnail_image:
        ImageUtility.scale_image(image.image_file.name)
        image.file = ImageUtility.thumbnail_path(image.image_file.name)
        image.save()

class Migration(migrations.Migration):
  dependencies = [
    ('gallery', '0015_image_thumbnail_image'),
  ]

  operations = [
    migrations.RunPython(add_thumbnail_to_images),
  ]
