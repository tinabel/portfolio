from django.shortcuts import render
from rest_framework import viewsets
from .models import Image, Series
from .serializers import ImageSerializer

def index(request):
    images = Image.objects.filter(is_featured=True)
    series = Series.objects.filter(is_featured=True)
    return render(request, 'index.html', {'featured_images': images, 'featured_series': series})

def artwork_view(request):
    all_series = Series.objects.all()
    return render(request, 'artwork.html', {'series': all_series})

def series_view(request, series_slug):
    series = Series.objects.get(slug=series_slug)
    images = Image.objects.filter(series_id=series.id)
    return render(request, 'series.html', {'series': series, 'series_images': images})

def image_view(request, series_slug, image_slug):
    image = Image.objects.filter(slug=image_slug)
    return render(request, 'image.html', {'image': image})

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    template_name = 'image.html'