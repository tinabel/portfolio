from io import BytesIO
import os
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from .image_utility import ImageUtility

class Medium(models.Model):
  name = models.CharField(max_length=255)
  slug = models.SlugField(blank=True)
  cover_image = models.ForeignKey('Image', on_delete=models.SET_NULL, null=True, blank=True, related_name='medium_cover')

  class Meta:
      verbose_name_plural = "media"

  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    return super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse("medium_view", kwargs={"slug": self.slug})

class Series(models.Model):
  title = models.CharField(max_length=255)
  cover_image = models.ForeignKey('Image', on_delete=models.SET_NULL, null=True, blank=True, related_name='series_cover')
  description = models.TextField(blank=True)
  medium = models.ForeignKey(Medium, on_delete=models.SET_NULL, null=True, blank=True)
  is_featured = models.BooleanField(default=False)
  slug = models.SlugField(blank=True)

  class Meta:
      verbose_name_plural = "series"

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("series", kwargs={"slug": self.slug})

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
    return super().save(*args, **kwargs)

class Image(models.Model):
  image_file = models.ImageField(upload_to='artwork', blank=True)
  thumbnail_image = models.ImageField(upload_to='thumbnails', blank=True)
  title = models.CharField(max_length=255)
  description = models.TextField(blank=True)
  alt = models.TextField(blank=True)
  medium = models.ForeignKey(Medium, on_delete=models.SET_NULL, null=True, blank=True)
  series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, blank=True)
  tags = models.CharField(max_length=255, blank=True)
  is_featured = models.BooleanField(default=False)
  slug = models.SlugField(blank=True)
  focal_point = models.CharField(
    max_length=255,
    choices=[
      ('', 'Focal Point'),
      ('bottom', 'Bottom Center'),
      ('bottom_left', 'Bottom Left'),
      ('bottom_right', 'Bottom Right'),
      ('center', 'Center'),
      ('left', 'Center Left'),
      ('right', 'Center Right'),
      ('top', 'Top Center'),
      ('top_left', 'Top Left'),
      ('top_right', 'Top Right'),
    ],
    default="center",
    blank=True
  )

  def get_filename(self):
    return os.path.basename(self.image_file.name) if self.image_file else None

  def get_description(self):
    return self.description

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
    return super(Image, self).save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse("image_view", kwargs={"slug": self.slug})
