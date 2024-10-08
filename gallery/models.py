import datetime
import os
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.html import mark_safe
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
  position = models.IntegerField(blank=True, null=True)

  class Meta:
      verbose_name_plural = "series"

  def images(self):
    Image.objects.filter(series_id=self.id)

  def cover(self):
    image = Image.objects.filter(series_id=self.cover_image).first()
    return image

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('series', kwargs={'slug': self.slug})

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
    return super().save(*args, **kwargs)

class Image(models.Model):
  image_focal_points=(
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
  )

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
  price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  print_size_height = models.IntegerField(blank=True, null=True)
  print_size_width = models.IntegerField(blank=True, null=True)
  image_focal_point = models.CharField(max_length=255, choices=image_focal_points, null=True, blank=True)

  def image_tag(self):
    url = settings.MEDIA_URL + self.thumbnail_image.name
    return mark_safe('<img src="%s" alt="" style="max-width: 300px; max-height: 300px;" />' % url)

  image_tag.short_description = 'Image'

  def get_filename(self):
    return os.path.basename(self.image_file.name) if self.image_file else None

  def get_description(self):
    return self.description

  def get_focal_point_class(self):
    if not self.image_focal_point:
      focal_point_classname = "center"
    else:
      focal_point_classname = self.image_focal_point.replace('_','-')
    return focal_point_classname

  def get_dominant_color(self):
    return ImageUtility.dominant_color(self.image_file.name)

  def low_quality_thumbnail_path(self):
    return ImageUtility.low_quality_path("thumbnail", self.thumbnail_image.name)

  def low_quality_full_size_image_path(self):
    return ImageUtility.low_quality_path("full", self.image_file.name)

  def print_dimensions(self):
    return f"{self.print_size_width}(inches wide) x {self.print_size_height}(inches high)"

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
    return super(Image, self).save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse("image_view", kwargs={'slug': self.slug})

class Page(models.Model):
  title = models.CharField(max_length=255)
  date = models.DateField(default=datetime.date.today)
  content = models.TextField()
  slug = models.SlugField(blank=True)

  def __str__(self):
    return self.title

class Cart(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  product = models.ForeignKey(Image, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1)

  def __str__(self):
    return f"{self.quantity} x {self.product.name}"

  def total_price(self):
    return self.quantity * self.product.price
