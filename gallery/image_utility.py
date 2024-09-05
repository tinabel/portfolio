from PIL import Image
from django.conf import settings
import os

class ImageUtility:
  def thumbnail_path(image_path):
    return os.path.join("/thumbnails", os.path.basename(image_path))


  def scale_image(image_path):
    """Resize an image to have a maximum size of 480px while preserving aspect ratio."""

    image_path = settings.MEDIA_ROOT + image_path

    with Image.open(image_path) as img:
        width, height = img.size

        if width < height:
            new_width = 480
            new_height = int((new_width / width) * height)
        else:
            new_height = 480
            new_width = int((new_height / height) * width)

        img = img.resize((new_width, new_height))
        img.save(ImageUtility.thumbnail_path(image_path), 'JPEG', quality=100)

