from PIL import Image
from django.conf import settings
import os

class ImageUtility:
  def thumbnail_path(image_path):
    return os.path.join(settings.MEDIA_ROOT,"thumbnails", os.path.basename(image_path))

  def low_quality_path(image_type, image_path):
    print(f"IMAGE PATH: {image_path}")
    image_directory = "artwork" if image_type == "full" else "thumbnails"
    print(image_directory)
    image_path = os.path.join(settings.MEDIA_ROOT, image_directory, os.path.basename(image_path))
    print(image_path)
    new_path = os.path.join(settings.MEDIA_ROOT, f"low-quality-{image_directory}", os.path.basename(image_path))
    relative_path = os.path.relpath(new_path, settings.MEDIA_ROOT)

    if not os.path.exists(new_path):
      img = Image.open(image_path)
      low_quality_img = img.copy()
      low_quality_img.save(new_path, 'webp', quality=30)

    return relative_path

  def dominant_color(image_path):
    image_path = os.path.join(settings.MEDIA_ROOT, image_path)
    pil_img = Image.open(image_path)
    img = pil_img.copy()
    img = img.convert("RGBA")
    img = img.resize((1, 1), resample=0)
    dominant_color = img.getpixel((0, 0))
    return dominant_color

  def scale_image(image_path):
    """Resize an image to have a maximum size of 480px while preserving aspect ratio."""

    image_path = settings.MEDIA_ROOT + '/' + image_path

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

