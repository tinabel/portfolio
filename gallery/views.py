from django.shortcuts import render
from rest_framework import viewsets
from .models import Image, Series
from .serializers import ImageSerializer
from .forms import ContactForm

def index(request):
  images = Image.objects.filter(is_featured=True)
  series = Series.objects.filter(is_featured=True).order_by('position')
  featured_series_image_ids = series.all().values_list('cover_image', flat = True)
  series_images = Image.objects.filter(id__in=featured_series_image_ids).order_by('series__position')

  return render(request, 'index.html', {'featured_images': images, 'featured_series': series, 'featured_series_images': series_images})

def artwork_view(request):
  all_series = Series.objects.all().order_by('position')
  series_image_ids = all_series.values_list('cover_image', flat = True)
  series_images = Image.objects.filter(id__in=series_image_ids).order_by('series__position')
  return render(request, 'artwork.html', {'series': all_series, 'series_images': series_images})

def series_view(request, series_slug):
  series = Series.objects.get(slug=series_slug)
  images = Image.objects.filter(series_id=series.id)
  return render(request, 'series.html', { 'series': series, 'series_images': images })

def image_view(request, series_slug, image_slug):
  image = Image.objects.get(slug=image_slug)
  return render(request, 'image.html', {'image': image, 'image_slug': image_slug })

def about_view(request):
  return render(request, 'about.html')

def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      pass
      return redirect('success')
  else:
    form = ContactForm()
  return render(request, 'contact.html', {'form': form})

def success(request):
  return HttpResponse('Your message was successfully sent. Thank you!')

class ImageViewSet(viewsets.ModelViewSet):
  queryset = Image.objects.all()
  serializer_class = ImageSerializer
  template_name = 'image.html'
