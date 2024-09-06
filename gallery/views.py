from django.shortcuts import render
from rest_framework import viewsets
from .models import Image, Series
from .serializers import ImageSerializer

def index(request):
  images = Image.objects.filter(is_featured=True)
  series = Series.objects.filter(is_featured=True, ordering='position')
  featured_series_image_ids = series.all().values_list('cover_image', flat = True)
  series_images = Image.objects.filter(id__in=featured_series_image_ids)

  return render(request, 'index.html', {'featured_images': images, 'featured_series': series, 'featured_series_images': series_images})

def artwork_view(request):
  all_series = Series.objects.all().order_by('position')
  series_image_ids = all_series.all().values_list('cover_image', flat = True)
  series_images = Image.objects.filter(id__in=series_image_ids)
  return render(request, 'artwork.html', {'series': all_series, 'series_images': series_images})

def series_view(request, series_slug):
  series = Series.objects.get(slug=series_slug)
  images = Image.objects.filter(series_id=series.id)
  return render(request, 'series.html', { 'series': series, 'series_images': images })

def image_view(request, series_slug, image_slug):
  image = Image.objects.filter(slug=image_slug)
  return render(request, 'image.html', {'image': image})

class ImageViewSet(viewsets.ModelViewSet):
  queryset = Image.objects.all()
  serializer_class = ImageSerializer
  template_name = 'image.html'
